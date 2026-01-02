import os
import atexit
import datetime
from pathlib import Path
from rbeesoftapps.common.logmanagerlistener import LogManagerListener
from rbeesoftapps.common.singleton import singleton


@singleton
class LogManager:
    def __init__(self, app_name: str=None, suppress_print: bool=False) -> None:
        self._suppress_print = suppress_print
        self._listeners = []
        file_path = os.path.join(Path.home(), f'{app_name}.log')
        self._file_handle = open(file_path, 'w', buffering=1)
        atexit.register(self.close_file)

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'[{timestamp}] {level} : {message}'
        if not self._suppress_print:
            print(message)
        self._file_handle.write(message + '\n')
        self.notify_listeners(message)
        return message

    def info(self, message):
        return self._log('INFO', message)

    def warning(self, message):
        return self._log('WARNING', message)

    def error(self, message):
        return self._log('ERROR', message)
    
    def add_listener(self, listener):
        if not isinstance(listener, LogManagerListener):
            raise ValueError(f'Listener {listener} is not a subclass of LogManagerListener')
        if listener not in self._listeners:
            self._listeners.append(listener)

    def notify_listeners(self, message):
        for listener in self._listeners:
            listener.new_message(message)

    def close_file(self):
        if self._file_handle:
            self._file_handle.close()