from customtkinter import CTk, CTkLabel, CTkSwitch, set_appearance_mode


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my Switch", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=10)

        self.switch = CTkSwitch(master=self, text="Dark Mode", command=self.callback)
        self.switch.pack(padx=20, pady=10)  

    def callback(self) -> None:
        value = self.switch.get()

        if value:
            set_appearance_mode("light")
            self.switch.configure(text="Light Mode")
        else:
            set_appearance_mode("dark")
            self.switch.configure(text="Dark Mode")
