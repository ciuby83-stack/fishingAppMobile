# routers/competitions.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import CompetitionCreate
from crud import create_competition

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_competition(competition: CompetitionCreate, event_id: int, db: Session = Depends(get_db)):
    return create_competition(db, competition, event_id)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_competition, get_competitions, create_score, get_scores_by_competition
from schemas import CompetitionCreate, CompetitionOut, ScoreCreate, ScoreOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Crează competiție
# -----------------------------
@router.post("/competitions/", response_model=CompetitionOut)
def add_competition(comp: CompetitionCreate, db: Session = Depends(get_db)):
    return create_competition(db, comp.name, comp.event_id, comp.max_participants)

# -----------------------------
# Lista competiții
# -----------------------------
@router.get("/competitions/", response_model=list[CompetitionOut])
def list_competitions(db: Session = Depends(get_db)):
    return get_competitions(db)

# -----------------------------
# Crează scor
# -----------------------------
@router.post("/scores/", response_model=ScoreOut)
def add_score(score: ScoreCreate, db: Session = Depends(get_db)):
    return create_score(db, score.user_id, score.competition_id, score.points)

# -----------------------------
# Lista scoruri după competiție
# -----------------------------
@router.get("/scores/{competition_id}", response_model=list[ScoreOut])
def list_scores(competition_id: int, db: Session = Depends(get_db)):
    return get_scores_by_competition(db, competition_id)
