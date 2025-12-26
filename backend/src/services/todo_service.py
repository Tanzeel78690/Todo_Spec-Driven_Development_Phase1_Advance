from typing import List, Optional
from uuid import UUID
from sqlmodel import Session, select
from backend.src.models.todo import Todo
from backend.src.models.user import User

def create_todo(session: Session, title: str, user: User) -> Todo:
    todo = Todo(title=title, owner_id=user.id)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def get_todos_by_user(session: Session, user: User) -> List[Todo]:
    return session.exec(select(Todo).where(Todo.owner_id == user.id)).all()

def get_todo_by_id_and_user(session: Session, todo_id: UUID, user: User) -> Optional[Todo]:
    return session.exec(select(Todo).where(Todo.id == todo_id, Todo.owner_id == user.id)).first()

def update_todo(session: Session, todo: Todo, title: Optional[str] = None, is_completed: Optional[bool] = None) -> Todo:
    if title is not None:
        todo.title = title
    if is_completed is not None:
        todo.is_completed = is_completed
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def delete_todo(session: Session, todo: Todo):
    session.delete(todo)
    session.commit()
