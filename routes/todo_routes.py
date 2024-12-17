from fastapi import APIRouter
from models.todo import Response, ResponseSingle, Todo, TodoUpdateRequest
from controllers.todo_controller import fetch_todos, fetch_todo, create_todo, finish_todo, update_todo, delete_todo

router = APIRouter(prefix="/api/v1/todos")

@router.get("", response_model=Response, responses = {
    200: {
        "description": "Fetched todos successfully",
        "content": {
            "application/json": {
                "example": 
                    { 
                        "data": [
                            {
                                "id": "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                                "title": "This is title",
                                "description": "This is description",
                                "finished_at": "null",
                                "created_at": "17/12/2024 15:41:38",
                                "updated_at": "17/12/2024 15:41:38",
                                "deleted_at": "null"
                            }
                        ],
                        "message": "Fetched todos successfully",
                        "error": "false"
                    }
            }
        }
    }})
async def get_todos():
    return fetch_todos()

@router.get("/{todo_id}", response_model=ResponseSingle, responses = {
    200: {
        "description": "Fetched todos successfully",
        "content": {
            "application/json": {
                "example": 
                    { 
                        "data": 
                            {
                                "id": "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                                "title": "This is title",
                                "description": "This is description",
                                "finished_at": "null",
                                "created_at": "17/12/2024 15:41:38",
                                "updated_at": "17/12/2024 15:41:38",
                                "deleted_at": "null"
                            }
                        ,
                        "message": "Fetched todo successfully",
                        "error": "false"
                    }
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
        "application/json": {
                "example": 
                    { 
                        "details": "Todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70 not found"
                    }
            }
        },
    }})
async def get_todo(todo_id: str):
    return fetch_todo(todo_id)

@router.post("", response_model=ResponseSingle, responses= {
    201: {
        "description": "Successfully created todo",
        "content": {
            "application/json": {
                "example": 
                    { 
                        "data": 
                            {
                                "id": "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                                "title": "This is title",
                                "description": "This is description",
                                "finished_at": "null",
                                "created_at": "17/12/2024 15:41:38",
                                "updated_at": "17/12/2024 15:41:38",
                                "deleted_at": "null"
                            }
                        ,
                        "message": "Successfully created todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                        "error": "false"
                    }
            }
        }
    }
}, status_code=201)
async def insert_todo(todo: Todo):
    return create_todo(todo)

@router.post("/{todo_id}/finish", response_model=ResponseSingle, responses= {
    200: {
        "description": "Fetched todos successfully",
        "content": {
            "application/json": {
                "example": 
                    { 
                        "data": [
                            {
                                "id": "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                                "title": "This is title",
                                "description": "This is description",
                                "finished_at": "17/12/2024 15:45:00",
                                "created_at": "17/12/2024 15:41:38",
                                "updated_at": "17/12/2024 15:41:38",
                                "deleted_at": "null"
                            },
                        ],
                        "message": "Fetched todo successfully",
                        "error": "false"
                    }
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
        "application/json": {
                "example": 
                    { 
                        "details": "Todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70 not found"
                    }
            }
        },
    }
})
async def mark_finished(todo_id: str):
    return finish_todo(todo_id)

@router.put("/{todo_id}", response_model=ResponseSingle, responses= {
    200: {
        "description": "Successfully updated todo",
        "content": {
            "application/json": {
                "example": 
                    { 
                        "data": [
                            {
                                "id": "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                                "title": "This is description",
                                "description": "This is title",
                                "finished_at": "17/12/2024 15:45:00",
                                "created_at": "17/12/2024 15:41:38",
                                "updated_at": "null",
                                "deleted_at": "null"
                            },
                        ],
                        "message": "Successfully updated todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                        "error": "false"
                    }
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
        "application/json": {
                "example": 
                    { 
                        "details": "Todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70 not found"
                    }
            }
        },
    }
})
async def edit_todo(todo_id: str, todo_update: TodoUpdateRequest):
    return update_todo(todo_id, todo_update)

@router.delete("/{todo_id}", response_model=ResponseSingle, responses= {
    200: {
        "description": "Successfully deleted todo",
        "content": {
            "application/json": {
                "example": 
                    { 
                        "data": 
                            {
                                "id": "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                                "title": "This is title",
                                "description": "This is description",
                                "finished_at": "null",
                                "created_at": "17/12/2024 15:41:38",
                                "updated_at": "17/12/2024 15:41:38",
                                "deleted_at": "17/12/2024 15:45:00"
                            }
                        ,
                        "message": "Successfully deleted todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70",
                        "error": "false"
                    }
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
        "application/json": {
                "example": 
                    { 
                        "details": "Todo with id: 0272802d-6e2b-40f7-834d-c66c9e9f9f70 not found"
                    }
            }
        },
    }
})
async def remove_todo(todo_id: str):
    return delete_todo(todo_id)
