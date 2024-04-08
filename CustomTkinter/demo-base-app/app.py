from typing import List

from customtkinter import CTk, CTkLabel, CTkScrollableFrame

from config.settings import AssetsImages
from utils.types import Task


class App(CTk):
    tasks: List[Task] = []

    def __init__(self) -> None:
        super().__init__()
        self.geometry("900x600")
        self.minsize(650, 400)
        self.title("Todo App")
        self.iconbitmap(AssetsImages.ICON)

        CTkLabel(master=self, text="Todo List App", font=("arial", 25, "bold")).pack(pady=20, padx=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
