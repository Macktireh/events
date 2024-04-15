from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGES_DIR = BASE_DIR / "assets" / "images"

BASE_API_URL = "http://localhost:8000"


class Color:
    TRANSPARENT = "transparent"
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY = "#CCCCCC"
    RED = "#c60101"
    ORANGE = "#d97706"
    GREEN = "#017a01"
    BLUE = "#035fa1"
    TEXT = ("#000000", "#FFFFFF")
    PRIMARY = ("#B665D3", "#B665D3")


class AssetsImages:
    ICON = IMAGES_DIR / "logo.ico"
    LOGO = IMAGES_DIR / "logo.png"
    EDIT_DARK = IMAGES_DIR / "edit-white.png"
    EDIT_LIGHT = IMAGES_DIR / "edit-black.png"
    CROSS_DARK = IMAGES_DIR / "cross-white.png"
    CROSS_LIGHT = IMAGES_DIR / "cross-black.png"
    ADD_DARK = IMAGES_DIR / "add-white.png"
    ADD_LIGHT = IMAGES_DIR / "add-black.png"
    OK_DARK = IMAGES_DIR / "ok-white.png"
    OK_LIGHT = IMAGES_DIR / "ok-black.png"
