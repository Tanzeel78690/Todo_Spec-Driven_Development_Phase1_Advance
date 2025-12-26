import logging
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from backend.src.database import create_db_and_tables
from backend.src.api import auth, todos

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup...")
    print("Creating DB and tables...")
    create_db_and_tables()
    yield
    logger.info("Application shutdown.")

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",  # Frontend development server
    "http://localhost:8000",  # Backend development server (if accessed directly)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}", exc_info=True)
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred"},
    )

app.include_router(auth.router)
app.include_router(todos.router, dependencies=[Depends(auth.get_current_user)])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Todo App Backend!"}
