from PySide6.QtCore import QSettings
from rbeesoftapps.common.logmanager import LogManager


class Settings(QSettings):
    def __init__(self, bundle_identifier: str, app_name: str):
        super(Settings, self).__init__(
            QSettings.IniFormat, 
            QSettings.UserScope, 
            bundle_identifier, 
            app_name,
        )
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._log = LogManager()

    def prepend_bundle_identifier_and_name(self, name):
        return '{}.{}.{}'.format(self._bundle_identifier, self._app_name, name)

    def get(self, name, default=None):
        if not name.startswith(self._bundle_identifier):
            name = self.prepend_bundle_identifier_and_name(name)
        value = self.value(name)
        if value is None or value == '':
            return default
        return value
    
    def get_int(self, name, default=None):
        try:
            return int(self.get(name, default))
        except ValueError as e:
            return default
        
    def get_float(self, name, default=None):
        try:
            return float(self.get(name, default))
        except ValueError as e:
            return default
        
    def get_bool(self, name, default=None):
        try:
            value = self.get(name, default)
            if value and isinstance(value, str):
                if value == '0' or value.lower() == 'false':
                    return False
                elif value == '1' or value.lower() == 'true':
                    return True
                else:
                    return default
            if value and isinstance(value, bool):
                return value
        except ValueError as e:
            return default
    
    def set(self, name, value):
        name = self.prepend_bundle_identifier_and_name(name)
        self.setValue(name, value)

    def print(self):
        self._log.info(f'Settings path: {self.fileName()}')
        for key in self.allKeys():
            self._log.info(f'Settings: {key}')