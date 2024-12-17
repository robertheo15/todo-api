from datetime import datetime
from pytz import timezone
from uuid import uuid4
from fastapi import HTTPException
from db.database import db
from models.todo import Todo, Response, ResponseSingle, TodoUpdateRequest

def fetch_todos():
    active_todos = [todo for todo in db.values() if todo.deleted_at is None]
    return Response(
        data=active_todos,
        message="Fetched todos successfully",
        error=False
    )

def fetch_todo(todo_id: str):
    if todo_id in db and db[todo_id].deleted_at is None:
        return ResponseSingle(
            data=db[todo_id],
            message="Fetched todo successfully",
            error=False
        )
    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

def create_todo(todo: Todo):
    todo.id = str(uuid4())
    todo.created_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S")
    todo.updated_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S")
    todo.deleted_at = None
    db[todo.id] = todo
    
    return ResponseSingle(
        message= f"Successfully created todo with id: {todo.id}",
        error= False,
        data= todo
    )

def finish_todo(todo_id: str):
    if todo_id in db:
        existing_todo = db[todo_id]
        if existing_todo.finished_at is not None:
            return ResponseSingle(
                message=f"Todo with id: {todo_id} already finished",
                error=False,
                data=existing_todo
            )

        existing_todo.finished_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S")
        db[todo_id] = existing_todo

        return ResponseSingle(
            message=f"Successfully finished todo with id: {todo_id}",
            error=False,
            data=existing_todo
        )
    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

def update_todo(todo_id: str, todo_update: TodoUpdateRequest):
    if todo_id in db:
        existing_todo = db[todo_id]

        if existing_todo.deleted_at is not None:
            raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")
        if todo_update.title is not None:
            existing_todo.title = todo_update.title
        if todo_update.description is not None:
            existing_todo.description = todo_update.description
            
        existing_todo.updated_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S")
        db[todo_id] = existing_todo

        return ResponseSingle(
            message=f"Successfully updated todo with id: {todo_id}",
            error=False,
            data=existing_todo
        )
    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

def delete_todo(todo_id: str):
    if todo_id in db:
        existing_todo = db[todo_id]
        if existing_todo.deleted_at is not None:
            raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

        existing_todo.deleted_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S")
        db[todo_id] = existing_todo

        return ResponseSingle(
            message=f"Successfully deleted todo with id: {todo_id}",
            error=False,
            data=existing_todo
        )
    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")
