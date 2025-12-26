from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

class Todo(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    title: str
    is_completed: bool = Field(default=False)
    owner_id: UUID = Field(foreign_key="user.id")

    owner: Optional["User"] = Relationship(back_populates="todos")
