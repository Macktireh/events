from typing import List

from utils.types import Task


def count_tasks_not_completed(tasks: List[Task]) -> int:
    return len(list(filter(lambda task: not task["completed"], tasks)))
