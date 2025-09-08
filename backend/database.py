# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Folosim SQLite pentru test, poți schimba cu PostgreSQL/MySQL după preferințe
SQLALCHEMY_DATABASE_URL = "sqlite:///./fishing_app.db"

# Creăm engine-ul SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal pentru a obține sesiuni DB în fiecare request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clasa de bază pentru modelele SQLAlchemy
Base = declarative_base()
