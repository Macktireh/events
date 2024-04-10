---
theme: dracula
layout: center
transition: slide-left
favicon: https://customtkinter.tomschimansky.com/img/icon.ico
title: Découverte de CustomTkinter
---

# Découvrir CustomTkinter

---
layout: center
class: 'text-white'
---

# Sommaire

<br>

1.  Qu’est-ce que CustomTkinter ?
2.  Pourquoi utiliser ?
3.  Création de votre première application CustomTkinter
4.  Démo d’une application complexe (avec auth, navigation, dashboard, …)
5.  Ressources pour en savoir plus

---
layout: center
class: 'text-white'
---

# Qui sui-je ?

<br>

- <carbon-user />  Macktireh Abdi Soubaneh
- <carbon-BaggageClaim /> Data Science > Développeur

---
layout: center
class: 'text-white'
---

<h1 style="display:flex; justify-content:center; gap:10px">
    Qu’est-ce que
</h1>

<h1 style="display:flex; justify-content:center; gap:10px">
    <img src="https://customtkinter.tomschimansky.com/img/icon.ico" width="40px" style="display:inline" />
    CustomTkinter ?
</h1>

<br>

- Librarie Python développée par Tom Schimansky

- Basé sur librarie standard de Python Tkinter

- https://github.com/tomschimansky/customtkinter ⭐ 10.1K

<br>
```bash
pip install customtkinter
```

---
layout: center
class: 'text-white'
---

<h1 style="display:flex; justify-content:center; gap:10px">
    Pourquoi
</h1>

<h1 style="display:flex; justify-content:center; gap:10px">
    <img src="https://customtkinter.tomschimansky.com/img/icon.ico" width="40px" style="display:inline" />
    CustomTkinter ?
</h1>

<br>

- Apprentissage facile : Si vous êtes déjà familier avec Tkinter, la transition vers CustomTkinter sera transparente

- Modernité des Widgets : CustomTkinter offre des widgets modernes et entièrement personnalisables.

- Thèmes d’Apparence : Il permet de configurer facilement le mode d’apparence du GUI, avec des options comme <code>système</code>, <code>sombre</code> et <code>clair</code>.

- Compatibilité : Il peut être utilisé en combinaison avec les éléments Tkinter classiques, offrant ainsi une grande flexibilité.


---
layout: center
class: 'text-white'
---

# Simple Application avec Tkinter

<div style="display:flex; justify-content:center; gap:10px">
<div>

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

</div>
<div style="display:flex; justify-content:center;align-items: center">

<img src="/images/tk.png" width="400px" style="display:flex; justify-content:center;align-items: center" />

</div>
</div>


---
layout: center
class: 'text-white'
---

# Avec CustomTkinter

<div style="display:flex; justify-content:center; gap:10px">
<div>

```py {1|4-14|17-19|all}
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

</div>
<div style="display:flex; justify-content:center;align-items: center">

<img src="/images/ctk.png" width="400px" style="display:flex; justify-content:center;align-items: center" />

</div>
</div>


---
layout: center
class: 'text-white'
---

<div style="display:flex; justify-content:center; gap:10px">
<div style="display:flex; justify-content: center; align-items: start; flex-direction: column">

## Tkinter


```py
from tkinter import Tk, Button


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My App")
        self.geometry("400x150")
        
        self.button = Button(
            self, text="my button", command=self.callback
        )
        self.button.pack(padx=20, pady=20)
    
    def callback(self) -> None:
        print("Hello World!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
```

</div>
<div style="display:flex; justify-content: center; align-items: start; flex-direction: column">

## CustomTkinter

```py
from customtkinter import CTk, CTkButton


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My App")
        self.geometry("400x150")
        
        self.button = CTkButton(
            self, text="my button", command=self.callback
        )
        self.button.pack(padx=20, pady=20)
    
    def callback(self) -> None:
        print("Hello World!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
```

</div>
</div>


---
layout: center
class: 'text-white'
---

# Live coding

---
layout: center
class: 'text-white'
---

# Démo d’une application complexe


---
layout: center
class: 'text-white'
---

# Pour en savoir plus

<br>

- Documentation officielle et tutoriel : [https://customtkinter.tomschimansky.com/](https://customtkinter.tomschimansky.com/)

- Tutoriel Youtube : [https://www.youtube.com/playlist?list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f](https://www.youtube.com/playlist?list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f)


---
layout: center
class: 'text-white'
---

# Merci !
