from tkinter import NORMAL, StringVar
from typing import Any, Callable, Optional, Tuple, Union

from customtkinter import CTkBaseClass, CTkEntry, CTkFont

from config.settings import Color


class Input(CTkEntry):
    def __init__(
        self,
        master: CTkBaseClass,
        width: int = 140,
        height: int = 28,
        corner_radius: Optional[int] = None,
        border_width: Optional[int] = None,
        bg_color: Union[str, Tuple[str, str]] = Color.TRANSPARENT,
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        border_color: Optional[Union[str, Tuple[str, str]]] = None,
        text_color: Optional[Union[str, Tuple[str, str]]] = None,
        placeholder_text_color: Optional[Union[str, Tuple[str, str]]] = None,
        placeholder_text: Union[str, None] = None,
        font: Optional[Union[tuple, CTkFont]] = None,
        state: str = NORMAL,
        default: Optional[str] = "",
        on_change: Optional[Callable[[StringVar], Any]] = None,
        **kwargs,
    ) -> None:
        self.on_change = on_change

        self.var = StringVar(value=default)
        self.var.trace_add("write", self.on_change_callback)

        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            placeholder_text_color=placeholder_text_color,
            textvariable=self.var,
            placeholder_text=placeholder_text,
            font=font,
            state=state,
            **kwargs,
        )

    def get_value(self) -> str:
        return self.var.get()

    def set_value(self, value: str) -> None:
        self.var.set(value)

    def reset(self) -> None:
        self.var.set("")
        self.update()

    def set_state(self, state: str) -> None:
        self.configure(state=state)

    def set_password(self, value: bool) -> None:
        if value:
            self.configure(show="●")
        else:
            self.configure(show="")

    def on_change_callback(self, *args: Tuple[Any, ...]) -> None:
        if self.on_change is not None:
            self.on_change(self.var)
            return
