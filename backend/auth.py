# auth.py
from passlib.context import CryptContext

# Context pentru criptarea parolelor
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -----------------------------
# Hash parole
# -----------------------------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# -----------------------------
# Verifică parola la login
# -----------------------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
