from fastapi import FastAPI

from app.controllers.auth_controller import router as auth_router
from app.controllers.user_controller import router as user_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Authentication Service"}
