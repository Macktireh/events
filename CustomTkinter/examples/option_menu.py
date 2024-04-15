from customtkinter import CTk, CTkLabel, CTkOptionMenu


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my OptionMenu", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=20)

        self.optionmenu = CTkOptionMenu(
            master=self, values=["option 1", "option 2"], command=self.callback
        )
        self.optionmenu.pack(padx=20, pady=20)

    def callback(self, choice) -> None:
        print("optionmenu dropdown clicked:", choice)
