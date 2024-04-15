from threading import Thread
from customtkinter import CTk, CTkLabel, CTkProgressBar


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("600x300")

        self.label = CTkLabel(master=self, text="my Progress bar", font=("Arial", 24, "bold"))
        self.label.pack(padx=20, pady=10)

        self.progressbar = CTkProgressBar(master=self, orientation="vertical")
        self.progressbar.pack(padx=20, pady=10)

        self.callback()

    def callback(self):
        def _funct(self):
            for i in range(1000):
                self.progressbar.set(i / 100)
                self.update()
        
        Thread(target=_funct, args=(self,)).start()
        
     


if __name__ == "__main__":
    app = App()
    app.mainloop()
