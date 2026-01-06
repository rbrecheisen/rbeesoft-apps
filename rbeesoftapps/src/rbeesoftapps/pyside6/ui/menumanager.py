from PySide6.QtWidgets import (
    QMenuBar,
    QMenu,
    QAction,
)


class MenuManager:
    def __init__(self, menu_bar: QMenuBar) -> None:
        self._menu_bar = menu_bar

    def create_menu(self, menu_path: str) -> QMenu:
        return None