from typing import List

from httpx import Client

from config.settings import BASE_API_URL
from utils.types import Task, TaskPayload


class TaskService:
    resource = "/tasks"

    def __init__(self) -> None:
        self.clinet = Client(base_url=BASE_API_URL)

    def addTask(self, newTask: Task) -> Task:
        return self.clinet.post(url=self.resource, json=newTask).json()

    def getTasks(self) -> List[Task]:
        return self.clinet.get(url=self.resource).json()

    def getTaskById(self, id: int) -> Task:
        return self.clinet.get(url=f"{self.resource}/{id}").json()

    def updateTask(self, id: int, payload: TaskPayload) -> Task:
        return self.clinet.patch(url=f"{self.resource}/{id}", json=payload).json()

    def deleteTask(self, id: int) -> None:
        self.clinet.delete(f"{self.resource}/{id}")
