from customtkinter import CTk, CTkLabel, CTkSlider


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my Slider", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=10)

        self.slider = CTkSlider(master=self, orientation="horizontal", command=self.callback)
        self.slider.pack(padx=20, pady=10)

    def callback(self, value) -> None:
        print(value)
