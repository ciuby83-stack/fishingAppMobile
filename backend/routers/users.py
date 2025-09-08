# routers/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate, UserOut
from crud import create_user, get_user_by_username, authenticate_user, create_access_token
from auth import hash_password, verify_password
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Register
# -----------------------------
@router.post("/users/", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = hash_password(user.password)
    new_user = create_user(db, user.username, user.email, hashed_pw)
    return new_user

# -----------------------------
# Login
# -----------------------------
@router.post("/users/login")
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    data = {"sub": user.username, "role": user.role}  # include rol în token
    token = create_access_token(data)
    return {"access_token": token, "token_type": "bearer"}

# -----------------------------
# Get current user din token
# -----------------------------
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# -----------------------------
# Dependență pentru rol
# -----------------------------
def require_role(required_role: str):
    def role_checker(current_user=Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User does not have {required_role} privileges"
            )
        return current_user
    return role_checker

@router.put("/users/{user_id}/activate")
def activate_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = True
    db.commit()
    db.refresh(user)
    return {"message": f"User {user.username} activated"}

@router.put("/users/{user_id}/deactivate")
def deactivate_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = False
    db.commit()
    db.refresh(user)
    return {"message": f"User {user.username} deactivated"}

@router.put("/users/{user_id}/role")
def set_user_role(user_id: int, role: str, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    if role not in ["user", "organizer", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role = role
    db.commit()
    db.refresh(user)
    return {"message": f"User {user.username} role updated to {role}"}
