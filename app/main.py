from fastapi import FastAPI
from app.api.game import router as game_router
from app.api.v1.endpoints import projects, users, tasks
from app.api import game

app = FastAPI()

app.include_router(game.router)
app.include_router(projects.router)  
app.include_router(users.router) 
app.include_router(tasks.router) 