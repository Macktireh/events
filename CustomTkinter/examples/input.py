from tkinter import StringVar
from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my Entry", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=10)

        self.var = StringVar(value="default value")
        self.var.trace_add("write", lambda *args: self.on_change())

        self.label2 = CTkLabel(master=self, text="my Entry", font=("Arial", 24, "bold"), textvariable=self.var)
        self.label2.pack(padx=20, pady=10)

        self.input = CTkEntry(master=self, textvariable=self.var)
        self.input.pack(padx=20, pady=10)

        self.button = CTkButton(
            master=self,
            text="my button",
            command=self.callback,
            fg_color="green",
            bg_color="red",
        )
        self.button.pack(padx=20, pady=20)

    def callback(self) -> None:
        print(self.input.get())

    def on_change(self) -> None:
        print("on change")
