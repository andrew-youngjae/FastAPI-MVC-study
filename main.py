from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from database import Base, engine
from controllers import router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

Base.metadata.create_all(bind=engine)
app.include_router(router)
templates = Jinja2Templates(directory="templates")