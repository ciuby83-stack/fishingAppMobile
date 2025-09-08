# routers/events.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_event, get_events
from schemas import EventCreate, EventOut
from routers.users import require_role, get_current_user  # import funcții roluri

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# POST /events/ – doar organizator
# -----------------------------
@router.post("/events/", response_model=EventOut)
def create_event_protected(event: EventCreate, db: Session = Depends(get_db), current_user=Depends(require_role("organizer"))):
    return create_event(db, event.name, event.description, current_user.id)

# -----------------------------
# GET /events/ – toate evenimentele
# -----------------------------
@router.get("/events/", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db)):
    return get_events(db)
