from typing import Callable

from customtkinter import CTkBaseClass, CTkButton, CTkFrame, CTkImage
from PIL import Image

from components.input import Input
from config.settings import AssetsImages, Color
from utils.types import TaskPayload


class AddTaskForm(CTkFrame):
    def __init__(
        self, master: CTkBaseClass, handle_add_task: Callable[[TaskPayload], None]
    ) -> None:
        self.master = master
        self.handle_add_task = handle_add_task

        super().__init__(master=self.master, fg_color=Color.TRANSPARENT, width=600, height=40)

        self.input = Input(master=self, placeholder_text="Titre")
        self.input.bind("<Return>", lambda _: self.add_new_task())
        self.input.place(relx=0.1, rely=0.05, relwidth=0.7, relheight=0.9)

        self.button = CTkButton(
            master=self,
            command=self.add_new_task,
            text="",
            image=CTkImage(
                dark_image=Image.open(AssetsImages.ADD_DARK),
                light_image=Image.open(AssetsImages.ADD_LIGHT),
                size=(20, 20),
            ),
            cursor="hand2",
            width=38,
            # height=35,
        )
        # self.button.pack(padx=10, side=RIGHT)
        self.button.place(relx=0.81, rely=0.05, relheight=0.9)

    def add_new_task(self) -> None:
        title = self.input.get_value()
        if not title:
            return
        newTask = TaskPayload(title=title, completed=False)
        self.handle_add_task(newTask)
        self.input.reset()
