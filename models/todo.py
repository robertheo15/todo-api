from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel

class Todo(BaseModel):
    id: Optional[str] = str(uuid4())
    title: str
    description: str
    finished_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None    

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title":  "This is title",
                    "description": "This is description"
                }
            ]
        }
    }

class Response(BaseModel):
    data: Optional[List[Todo]] = None
    message: str
    error: bool

class ResponseSingle(BaseModel):
    data: Optional[Todo] = None
    message: str
    error: bool

class TodoUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title":  "This is description",
                    "description": "This is title"
                }
            ]
        }
    }