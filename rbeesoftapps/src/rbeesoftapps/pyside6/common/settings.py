import os
import json
import atexit
from pathlib import Path
from rbeesoftapps.common.singleton import singleton


@singleton
class Settings:
    def __init__(self, bundle_identifier: str=None, app_name: str=None) -> None:
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._file_path = os.path.join(Path.home(), f'{self._app_name}.settings')
        self._settings = self.load_or_initialize_settings(self._file_path)
        atexit.register(self.close_file)

    def load_or_initialize_settings(self, file_path):
        file_exists = os.path.isfile(file_path)
        if file_exists:
            with open(file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.decoder.JSONDecodeError:
                    pass
        return {
            self._bundle_identifier: {
                self._app_name: {
                }
            }
        }        

    def check_bundle_identifier_and_app_name(self):
        if not self._bundle_identifier or not self._app_name:
            raise ValueError(f'Settings bundle identifier or app name not set')
        
    def get(self, name, default=None):
        self.check_bundle_identifier_and_app_name()
        if not name in self._settings[self._bundle_identifier][self._app_name].keys():
            return default
        return self._settings[self._bundle_identifier][self._app_name][name]
    
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
        self.check_bundle_identifier_and_app_name()
        self._settings[self._bundle_identifier][self._app_name][name] = value

    def print(self):
        self.check_bundle_identifier_and_app_name()
        if self._settings:
            text = json.dumps(self._settings, indent=2, sort_keys=True)
            print(text)
            return text
        return None

    def close_file(self):
        self.check_bundle_identifier_and_app_name()
        if self._settings:
            with open(self._file_path, 'w') as f:
                json.dump(self._settings, f, indent=2)