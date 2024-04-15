from customtkinter import CTk, CTkLabel, CTkTabview


class MyTabView(CTkTabview):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self.language = "Programming language"
        self.framework = "Framework"
        self.sport = "Sport"

        # create tabs
        self.add(name=self.language)
        self.add(name=self.framework)
        self.add(name=self.sport)

        # add widgets on tabs
        CTkLabel(master=self.tab(name=self.language), text="Python").grid(row=0, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.language), text="Java").grid(row=1, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.language), text="C++").grid(row=2, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.language), text="JavaScript").grid(row=3, column=0, padx=20, pady=10)

        CTkLabel(master=self.tab(name=self.framework), text="Django").grid(row=0, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.framework), text="Angular").grid(row=1, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.framework), text="Laravel").grid(row=2, column=0, padx=20, pady=10)

        CTkLabel(master=self.tab(name=self.sport), text="Tennis").grid(row=0, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.sport), text="MMA").grid(row=1, column=0, padx=20, pady=10)
        CTkLabel(master=self.tab(name=self.sport), text="Football").grid(row=2, column=0, padx=20, pady=10)


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#2f343f")
        self.title("My App")
        self.geometry("800x500")

        self.label = CTkLabel(master=self, text="my TabView", font=("Arial", 24, "bold"))
        self.label.place(relx=0.5, rely=0.08, anchor="center")

        self.tab_view = MyTabView(master=self)
        self.tab_view.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.75, anchor="center") 
