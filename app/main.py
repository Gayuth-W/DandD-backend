from fastapi import FastAPI
from app.core.config import APP_NAME
from app.api.v1.router import router

app = FastAPI(title=APP_NAME)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(router, prefix="/api")