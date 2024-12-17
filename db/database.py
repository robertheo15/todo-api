from typing import Dict
from datetime import datetime
from pytz import timezone
from models.todo import Todo
from pydantic import BaseModel

db: Dict[str, Todo] = {
    "0272802d-6e2b-40f7-834d-c66c9e9f9f70": Todo(
        id = "0272802d-6e2b-40f7-834d-c66c9e9f9f70",
        title = "This is title",
        description = "This is description",
        finished_at = None,
        created_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S"),
        updated_at = datetime.now(timezone("Asia/Jakarta")).strftime("%d/%m/%Y %H:%M:%S"),
        deleted_at = None
    ),
}