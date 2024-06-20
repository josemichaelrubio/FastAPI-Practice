from fastapi import FastAPI
import models
from database import engine

from routers import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# TODO: Authenication and Authorization enables with Tokens
# TODO: LOOK into alembic
