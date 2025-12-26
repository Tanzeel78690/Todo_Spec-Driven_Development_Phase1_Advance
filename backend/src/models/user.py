from typing import List, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str

    todos: List["Todo"] = Relationship(back_populates="owner")
