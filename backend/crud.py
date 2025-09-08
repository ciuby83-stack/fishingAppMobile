# crud.py
from sqlalchemy.orm import Session
from models import User
from auth import verify_password
from datetime import datetime, timedelta
from jose import jwt

# Secret pentru JWT (în producție folosește variabilă de mediu)
SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 oră

# -----------------------------
# Crează un user
# -----------------------------
def create_user(db: Session, username: str, email: str, hashed_pw: str):
    db_user = User(username=username, email=email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# -----------------------------
# Caută user după username
# -----------------------------
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# -----------------------------
# Authenticate user pentru login
# -----------------------------
def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# -----------------------------
# Creează access token JWT
# -----------------------------
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

from models import Event  # importă modelul Event din models.py

# -----------------------------
# Crează un eveniment
# -----------------------------
def create_event(db: Session, name: str, description: str, organizer_id: int):
    new_event = Event(
        name=name,
        description=description,
        organizer_id=organizer_id
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# -----------------------------
# Ia toate evenimentele
# -----------------------------
def get_events(db: Session):
    return db.query(Event).all()

from models import Competition, Score

# -----------------------------
# Crează competiție
# -----------------------------
def create_competition(db: Session, name: str, event_id: int, max_participants: int | None = None):
    comp = Competition(name=name, event_id=event_id, max_participants=max_participants)
    db.add(comp)
    db.commit()
    db.refresh(comp)
    return comp

# -----------------------------
# Ia toate competițiile
# -----------------------------
def get_competitions(db: Session):
    return db.query(Competition).all()

# -----------------------------
# Crează scor pentru user
# -----------------------------
def create_score(db: Session, user_id: int, competition_id: int, points: float):
    score = Score(user_id=user_id, competition_id=competition_id, points=points)
    db.add(score)
    db.commit()
    db.refresh(score)
    return score

# -----------------------------
# Lista scoruri pentru o competiție
# -----------------------------
def get_scores_by_competition(db: Session, competition_id: int):
    return db.query(Score).filter(Score.competition_id == competition_id).all()

def get_user_role(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if user:
        return user.role
    return None
