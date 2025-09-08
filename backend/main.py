# main.py
from fastapi import FastAPI
from database import Base, engine
from routers import users, events, competitions

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fishing App API",
    description="API pentru aplicația de pescuit cu user, organizatori și admin",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(competitions.router, prefix="/competitions", tags=["competitions"])

@app.get("/")
def read_root():
    return {"message": "Backend Fishing App funcționează!"}

from routers import users, events

app.include_router(users.router)
app.include_router(events.router)

from fastapi import FastAPI
from routers import users, events, competitions

app = FastAPI(title="Fishing App API", version="1.0.0")

app.include_router(users.router)
app.include_router(events.router)
app.include_router(competitions.router)

from fastapi import FastAPI
from routers import users, events, competitions

app = FastAPI(title="Fishing App API", version="1.0.0")

app.include_router(users.router)
app.include_router(events.router)
app.include_router(competitions.router)
