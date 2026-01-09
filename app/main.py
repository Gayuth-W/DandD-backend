# app/main.py
from fastapi import FastAPI
from app.api.game import router as game_router
from app.api.v1.endpoints import projects, users, tasks, admin, auth
from app.api import game

app = FastAPI()

@app.on_event("startup")
def startup():
  from app.core.database import SessionLocal
  from app.core.bootstrap import create_admin_if_not_exists
  
  db=SessionLocal()
  create_admin_if_not_exists(db)
  db.close()
  
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game.router) 
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(projects.router)  
app.include_router(users.router) 
app.include_router(tasks.router) 

