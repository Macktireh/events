# from threading import Thread
# from typing import List

# from customtkinter import CTk, CTkLabel, CTkScrollableFrame

# from components.addTaskForm import AddTaskForm
# from components.taskCounter import TaskCounter
# from components.taskItems import TaskItem
# from config.settings import AssetsImages, Color
# from services.taskService import TaskService
# from utils import count_tasks_not_completed
# from utils.types import Task, TaskPayload


# class App(CTk):
#     tasks: List[Task] = []

#     def __init__(self) -> None:
#         super().__init__()
#         self.geometry("900x600")
#         self.minsize(650, 400)
#         self.title("Todo App")
#         self.iconbitmap(AssetsImages.ICON)
#         self.task_service = TaskService()

#         CTkLabel(master=self, text="Todo List App", font=("arial", 25, "bold")).pack(pady=20, padx=20)
#         TaskCounter(master=self).pack(pady=10, padx=15)
#         AddTaskForm(master=self, handle_add_task=self.handle_add_task).pack(pady=10, padx=15)

#         self.container = CTkScrollableFrame(master=self, fg_color=Color.TRANSPARENT)
#         self.container.pack(padx=30, pady=(10, 30), expand=True, fill="both")

#         self.get_tasks()

#     def render_tasks(self) -> None:
#         for task in self.tasks:
#             TaskItem(
#                 master=self.container,
#                 task=task,
#                 on_edit_callback=self.on_edit_callback,
#                 on_delete_callback=self.on_delete_callback,
#             ).pack(padx=10, pady=5, fill="x")

#     def get_tasks(self) -> None:
#         def _func(self: App) -> None:
#             self.tasks = self.task_service.getTasks()
#             self.update_task_counter()
#             self.render_tasks()

#         Thread(target=_func, args=(self,)).start()

#     def handle_add_task(self, payload: TaskPayload) -> None:
#         def _func(self: App) -> None:
#             new_task = self.task_service.addTask(payload)
#             self.tasks.append(new_task)
#             TaskItem(
#                 master=self.container,
#                 task=new_task,
#                 on_edit_callback=self.on_edit_callback,
#                 on_delete_callback=self.on_delete_callback,
#             ).pack(padx=10, pady=5, fill="x")
#             self.update_task_counter()

#         Thread(target=_func, args=(self,)).start()

#     def on_edit_callback(self, id: int, payload: TaskPayload) -> None:
#         def _func(self: App) -> None:
#             task_updated = self.task_service.updateTask(id, payload)
#             self.tasks = list(map(lambda task: task if task["id"] != id else task_updated, self.tasks))
#             self.update_task_counter()

#         Thread(target=_func, args=(self,)).start()

#     def on_delete_callback(self, id: int, name: str) -> None:
#         self.task_service.deleteTask(id)
#         self.container.nametowidget(name).destroy()
#         self.tasks = list(filter(lambda task: task["id"] != id, self.tasks))
#         self.update_task_counter()

#     def update_task_counter(self) -> None:
#         count = count_tasks_not_completed(self.tasks)
#         self.nametowidget(".!taskcounter").configure(text=f"Tâches à faire : {count}")


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


from tkinter import Tk, Button


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My App")
        self.geometry("400x150")
        
        self.button = Button(self, text="my button", command=self.callback)
        self.button.pack(padx=20, pady=20)
    
    def callback(self) -> None:
        print("Hello World!")


if __name__ == "__main__":
    app = App()
    app.mainloop()