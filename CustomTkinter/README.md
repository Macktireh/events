<p style="display:flex; justify-content:center; gap:10px">
    <img src="https://customtkinter.tomschimansky.com/img/icon.ico" width="300px" style="display:inline" />
</p>
<h1 style="display:flex; justify-content:center; gap:10px">
    Découverte de CustomTkinter
</h1>


## Sommaire

1.  Qu’est-ce que CustomTkinter ?
2.  Pourquoi utiliser ?
3.  Installation
3.  Démo code
4.  Démo Application réelle (avec auth, navigation, dashboard, …)
5.  Ressources pour en savoir plus


## Qu’est-ce que ?

- Librarie Python développée par Tom Schimansky
- Basé sur librarie standard de Python Tkinter
- https://github.com/tomschimansky/customtkinter ⭐ 10.1K


## Pourquoi utiliser ?

- Apprentissage facile : Si vous êtes déjà familier avec Tkinter, la transition vers CustomTkinter sera transparente

- Modernité des Widgets : CustomTkinter offre des widgets modernes et entièrement personnalisables.

- Thèmes d’Apparence : Il permet de configurer facilement le mode d’apparence du GUI, avec des options comme <code>système</code>, <code>sombre</code> et <code>clair</code>.

- Compatibilité : Il peut être utilisé en combinaison avec les éléments Tkinter classiques, offrant ainsi une grande flexibilité.


## Installation

```bash
pip install customtkinter
```

## Simple Application avec Tkinter


```py
from tkinter import Tk, Button


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My App")
        self.geometry("400x150")
        
        self.button = Button(self, text="my button", command=self.callback)
        self.button.pack(padx=20, pady=20)
    
    def callback(self) -> None:
        print("Hello World!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
```


## Avec CustomTkinter

```py
from customtkinter import CTk, CTkButton


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My App")
        self.geometry("400x150")
        
        self.button = CTkButton(self, text="my button", command=self.callback)
        self.button.pack(padx=20, pady=20)
    
    def callback(self) -> None:
        print("Hello World!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
```

## Pour en savoir plus

- Documentation officielle et tutoriel : [https://customtkinter.tomschimansky.com/](https://customtkinter.tomschimansky.com/)

- Tutoriel Youtube : [https://www.youtube.com/playlist?list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f](https://www.youtube.com/playlist?list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f)