from customtkinter import CTkBaseClass, CTkLabel, StringVar

from utils import count_tasks_not_completed


class TaskCounter(CTkLabel):
    def __init__(self, master: CTkBaseClass) -> None:
        self.master = master
        self.count = count_tasks_not_completed(self.master.tasks)
        self.text_label = StringVar(value=f"Tâches à faire : {self.count}")

        super().__init__(
            self.master,
            text=self.text_label.get(),
            font=("arial", 20, "bold"),
            text_color=("#000", "#FFF"),
        )
