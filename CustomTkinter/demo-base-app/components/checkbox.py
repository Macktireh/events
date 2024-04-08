from typing import Any, Callable, Optional, Tuple, Union

from customtkinter import CTkBaseClass, CTkCheckBox, CTkFont, NORMAL, BooleanVar, Variable

from config.settings import Color


class Checkbox(CTkCheckBox):
    def __init__(
        self,
        master: CTkBaseClass,
        width: int = 100,
        height: int = 24,
        checkbox_width: int = 24,
        checkbox_height: int = 24,
        corner_radius: Optional[int] = None,
        border_width: Optional[int] = None,

        bg_color: Union[str, Tuple[str, str]] = Color.TRANSPARENT,
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        hover_color: Optional[Union[str, Tuple[str, str]]] = None,
        border_color: Optional[Union[str, Tuple[str, str]]] = None,
        checkmark_color: Optional[Union[str, Tuple[str, str]]] = None,
        text_color: Optional[Union[str, Tuple[str, str]]] = None,
        text_color_disabled: Optional[Union[str, Tuple[str, str]]] = None,

        text: str = "",
        font: Optional[Union[tuple, CTkFont]] = None,
        textvariable: Union[Variable, None] = None,
        state: str = NORMAL,
        cursor="hand2",
        hover: bool = True,
        command: Union[Callable[[], Any], None] = None,
        onvalue: bool = True,
        offvalue: bool = False,
        default: bool = False,
        on_change: Optional[Callable[[BooleanVar], Any | None]] = None,
        **kwargs,
    ) -> None:
        self.on_change = on_change

        self.var = BooleanVar(value=default)

        super().__init__(
            master=master,
            width=width,
            height=height,
            checkbox_width=checkbox_width,
            checkbox_height=checkbox_height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            checkmark_color=checkmark_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            text=text,
            font=font,
            textvariable=textvariable,
            state=state,
            cursor=cursor,
            hover=hover,
            command=command,
            onvalue=onvalue,
            offvalue=offvalue,
            variable=self.var,
            **kwargs,
        )

    def get_value(self) -> str:
        return self.var.get()

    def set_value(self, value: str) -> None:
        self.var.set(value)

    def reset(self) -> None:
        self.var.set(False)
        self.update()

    def on_change_callback(self, *args: Tuple[Any, ...]) -> None:
        if self.on_change is not None:
            self.on_change(self.var)
