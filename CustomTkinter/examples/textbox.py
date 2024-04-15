from customtkinter import CTk, CTkTextbox, CTkLabel


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my Textbox", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=10)

        self.textarea = CTkTextbox(master=self)
        self.textarea.pack(padx=20, pady=10, fill="x", expand=True)
