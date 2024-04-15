from customtkinter import CTk, CTkButton, CTkLabel


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my Button", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=20)

        self.button = CTkButton(
            master=self,
            text="my button",
            command=self.callback,
            fg_color="green",
            bg_color="red",
        )
        self.button.pack(padx=20, pady=20)

    def callback(self) -> None:
        print("Hello World!")
