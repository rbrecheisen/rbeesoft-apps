from PySide6.QtWidgets import (
    QMenuBar,
    QMenu,
)
from PySide6.QtGui import QAction


# https://chatgpt.com/c/695d07c5-6168-832d-beb9-08533aca7328
class MenuManager:
    def __init__(self, menu_bar: QMenuBar) -> None:
        self._menu_bar = menu_bar

    def create_menu(self, menu_path: str) -> QMenu:
        return None