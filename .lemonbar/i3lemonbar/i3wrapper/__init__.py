from .. import Scheduler
from threading import Thread

import i3ipc
import time


class i3Wrapper(object):
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler
        self.i3 = None
        self.i3_thread = None
        self.listeners = {
            'ipc_shutdown': [self._on_shutdown]
        }

    def on(self, name, listener):
        if name not in self.listeners:
            self.listeners[name] = []
            # Probably not registered during init
            if self.i3 is not None:
                self.i3.on(name, self._trigger_listeners)
        self.listeners[name].append(listener)

    def connected(self) -> bool:
        return self.i3 is not None

    def connect(self):
        while True:
            try:
                if self.i3 is None:
                    self.i3 = self.init_i3()
                if self.i3_thread is None:
                    self.i3_thread = self.init_i3_thread(self.i3)
                break
            except FileNotFoundError:
                time.sleep(1)

    def reconnect(self):
        if self.i3 is not None:
            self.i3.main_quit()
            if self.i3_thread is not None:
                self.i3_thread.join()
            self.i3 = None
        self.connect()

    def init_i3(self) -> i3ipc.Connection:
        i3 = i3ipc.Connection()
        for name in self.listeners.keys():
            i3.on(name, self.trigger_listeners(name))
        return i3

    def init_i3_thread(self, i3: i3ipc.Connection):
        thread = Thread(target=i3.main, name='i3 IPC Thread')
        thread.daemon = True
        thread.start()
        return thread

    def _trigger_listeners(self, name):
        if name not in self.listeners:
            return

        def wrapper_listener(*args):
            for listener in self.listeners[name]:
                listener(*args)
            self.scheduler.event.set()
        return wrapper_listener

    def _on_shutdown(self, i3: i3ipc.Connection):
        self.reconnect()
