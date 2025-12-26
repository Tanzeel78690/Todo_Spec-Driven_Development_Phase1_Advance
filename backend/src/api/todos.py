from typing import List, Optional, Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, SQLModel

from backend.src.database import get_session
from backend.src.models.todo import Todo
from backend.src.models.user import User
from backend.src.services import todo_service
from backend.src.api.auth import get_current_user

router = APIRouter(prefix="/api")

class TodoCreate(SQLModel):
    title: str

class TodoResponse(SQLModel):
    id: UUID
    title: str
    is_completed: bool
    owner_id: UUID

class TodoUpdate(SQLModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

@router.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_new_todo(
    todo_create: TodoCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    todo = todo_service.create_todo(session, todo_create.title, current_user)
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        is_completed=todo.is_completed,
        owner_id=todo.owner_id
    )

@router.get("/todos", response_model=List[TodoResponse])
async def read_todos(
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    todos = todo_service.get_todos_by_user(session, current_user)
    return [
        TodoResponse(
            id=todo.id,
            title=todo.title,
            is_completed=todo.is_completed,
            owner_id=todo.owner_id
        ) for todo in todos
    ]

@router.get("/todos/{todo_id}", response_model=TodoResponse)
async def read_todo(
    todo_id: UUID,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    todo = todo_service.get_todo_by_id_and_user(session, todo_id, current_user)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        is_completed=todo.is_completed,
        owner_id=todo.owner_id
    )

@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_existing_todo(
    todo_id: UUID,
    todo_update: TodoUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    todo = todo_service.get_todo_by_id_and_user(session, todo_id, current_user)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    
    updated_todo = todo_service.update_todo(session, todo, todo_update.title, todo_update.is_completed)
    return TodoResponse(
        id=updated_todo.id,
        title=updated_todo.title,
        is_completed=updated_todo.is_completed,
        owner_id=updated_todo.owner_id
    )

    

@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_existing_todo(

    todo_id: UUID,

    current_user: Annotated[User, Depends(get_current_user)],

    session: Annotated[Session, Depends(get_session)]

):

    todo = todo_service.get_todo_by_id_and_user(session, todo_id, current_user)

    if not todo:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    

    todo_service.delete_todo(session, todo)

    return



@router.patch("/todos/{todo_id}/complete", response_model=TodoResponse)

async def toggle_todo_completion(

    todo_id: UUID,

    current_user: Annotated[User, Depends(get_current_user)],

    session: Annotated[Session, Depends(get_session)]

):

    todo = todo_service.get_todo_by_id_and_user(session, todo_id, current_user)

    if not todo:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    

    updated_todo = todo_service.update_todo(session, todo, is_completed=not todo.is_completed)

    return TodoResponse(

        id=updated_todo.id,

        title=updated_todo.title,

        is_completed=updated_todo.is_completed,

        owner_id=updated_todo.owner_id

    )
