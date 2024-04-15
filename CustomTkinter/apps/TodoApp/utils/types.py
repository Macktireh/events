from typing import Optional, TypedDict


class Task(TypedDict):
    id: int
    title: str
    completed: bool


class TaskPayload(TypedDict):
    title: Optional[str]
    completed: Optional[bool]
