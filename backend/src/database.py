from sqlmodel import create_engine, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://user:password@localhost:5432/db_name")

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    # SQLModel.metadata.create_all(engine)
    # This will be called after models are defined
    pass

def get_session():
    with Session(engine) as session:
        yield session
