from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from database import Base, engine
from controllers import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # execute when application started
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # execute when application finished

# Initialize FastAPI Application
# Deactivate Swagger UI and Redoc
app = FastAPI(lifespan=app_lifespan, docs_url=None, redoc_url=None)
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
app.include_router(router)
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})