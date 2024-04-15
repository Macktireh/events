from typing import List
from customtkinter import CTkBaseClass, CTkLabel, StringVar

from utils import count_tasks_not_completed
from utils.types import Task


class TaskCounter(CTkLabel):
    def __init__(self, master: CTkBaseClass, tasks: List[Task]) -> None:
        self.master = master
        self.count = count_tasks_not_completed(tasks)
        self.text_label = StringVar(value=f"Tâches à faire : {self.count}")

        super().__init__(
            self.master,
            text=self.text_label.get(),
            font=("arial", 20, "bold"),
            text_color=("#000", "#FFF"),
        )
