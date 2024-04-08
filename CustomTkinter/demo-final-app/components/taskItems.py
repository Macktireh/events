from typing import Callable

from customtkinter import CTkButton, CTkImage, CTkFrame, CTkScrollableFrame, CTkLabel, LEFT, RIGHT
from PIL import Image

from components.checkbox import Checkbox
from components.input import Input
from config.settings import AssetsImages, Color
from utils.types import Task, TaskPayload


class TaskItem(CTkFrame):
    def __init__(
        self,
        master: CTkScrollableFrame,
        task: Task,
        on_edit_callback: Callable[[int, TaskPayload], None],
        on_delete_callback: Callable[[int, str], None],
    ) -> None:
        self.master = master
        self.task = task
        self.on_edit_callback = on_edit_callback
        self.on_delete_callback = on_delete_callback
        self.isEditing = False

        super().__init__(master=self.master, width=610, height=50, fg_color=Color.TRANSPARENT)

        self.checkbox = Checkbox(
            master=self,
            width=50,
            default=self.task["completed"],
            command=self.update_task_completed,
        )
        self.checkbox.place(relx=0.02, rely=0.1, relheight=0.8)

        self.label = CTkLabel(
            master=self,
            text=self.task["title"],
            font=("arial", 18, "bold"),
            compound=LEFT,
            anchor="w",
        )
        self.label.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.8)

        self.boxInput = CTkFrame(self, fg_color=Color.TRANSPARENT)
        self.input = Input(master=self.boxInput, placeholder_text="Title", default=self.task["title"])
        self.input.pack(fill="both", side=LEFT, expand=True)
        self.input.bind("<Return>", lambda _: self.update_task_title())
        self.okButton = CTkButton(
            master=self.boxInput,
            command=self.update_task_title,
            text="",
            image=CTkImage(
                dark_image=Image.open(AssetsImages.OK_DARK),
                light_image=Image.open(AssetsImages.OK_LIGHT),
                size=(20, 20),
            ),
            width=30,
            cursor="hand2",
        )
        self.okButton.pack(side=LEFT)

        self.boxButton = CTkFrame(master=self, height=50, fg_color=Color.TRANSPARENT)
        self.boxButton.pack(side=RIGHT, padx=(5, 10))
        self.editButton = CTkButton(
            master=self.boxButton,
            text="",
            command=self.toggle_editing,
            image=CTkImage(
                dark_image=Image.open(AssetsImages.EDIT_DARK),
                light_image=Image.open(AssetsImages.EDIT_LIGHT),
                size=(20, 20),
            ),
            width=30,
            height=30,
            fg_color=Color.TRANSPARENT,
            hover_color=("#9E9E9E", "#424242"),
            cursor="hand2",
        )
        self.editButton.grid(row=0, column=0, padx=2, pady=2)
        self.deleteButton = CTkButton(
            master=self.boxButton,
            text="",
            command=self.delete_task,
            image=CTkImage(
                dark_image=Image.open(AssetsImages.CROSS_DARK),
                light_image=Image.open(AssetsImages.CROSS_LIGHT),
                size=(20, 20),
            ),
            width=30,
            height=30,
            fg_color=Color.TRANSPARENT,
            hover_color=("#f82e57", "#f82e57"),
            cursor="hand2",
        )
        self.deleteButton.grid(row=0, column=1, padx=2, pady=2)        

    def toggle_editing(self) -> None:
        if self.isEditing:
            self.boxInput.place_forget()
            self.label.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.8)
        else:
            self.label.place_forget()
            self.boxInput.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.8)
            self.input.focus()

        self.isEditing = not self.isEditing

    def update_task_title(self) -> None:
        payload = TaskPayload(title=self.input.get_value())
        self.label.configure(text=payload["title"])
        self.on_edit_callback(self.task["id"], payload)
        self.toggle_editing()

    def update_task_completed(self) -> None:
        payload = TaskPayload(completed=self.checkbox.get_value())
        self.on_edit_callback(self.task["id"], payload)

    def delete_task(self) -> None:
        self.on_delete_callback(self.task["id"], self.winfo_name())
