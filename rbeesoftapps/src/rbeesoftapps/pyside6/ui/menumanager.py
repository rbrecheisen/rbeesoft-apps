from PySide6.QtWidgets import (
    QMenuBar,
    QMenu,
)


# https://chatgpt.com/c/695d07c5-6168-832d-beb9-08533aca7328
class MenuManager:
    def __init__(self, menu_bar: QMenuBar) -> None:
        self._menu_bar = menu_bar

    def _find_menu(self, title: str, parent_menu: QMenu=None) -> QMenu|None:
        if parent_menu is None:
            for action in self._menu_bar.actions():
                action_menu = action.menu()
                if action_menu is not None and action_menu.title().replace('&', '') == title:
                    return action_menu
            return None
        else:
            for action in parent_menu.actions():
                action_menu = action.menu()
                if action_menu is not None and action_menu.title().replace('&', '') == title:
                    return action_menu
            return None

    def create_menu(self, menu_path: str, sep: str='/') -> QMenu:
        parts = [p.strip() for p in menu_path.split(sep) if p.strip()]
        if not parts:
            raise ValueError('Empty menu path')
        menu = self._find_menu(title=parts[0])
        if menu is None:
            menu = self._menu_bar.addMenu(parts[0])
        for title in parts[1:]:
            child_menu = self._find_menu(title=title, parent_menu=menu)
            if child_menu is None:
                child_menu = menu.addMenu(title)
            menu = child_menu
        return menu