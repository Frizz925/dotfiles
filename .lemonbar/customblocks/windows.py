from i3lemonbar import Block, Scheduler
from i3lemonbar.containers import inject
from threading import Thread

import i3ipc


@inject(Scheduler)
class Windows(Block):
    def __init__(self, scheduler: Scheduler):
        self.i3 = None
        self.state = None
        self.last_state = None

    def should_update(self) -> bool:
        return self.i3 is None or self.state != self.last_state

    def render(self) -> str:
        self.check_init()
        if self.i3 is None:
            return ''
        self.last_state = self.state
        if self.state is None:
            focused = self.i3.get_tree().find_focused()
            self.state = focused.name
        return self.format(self.state)

    def format(self, text: str) -> str:
        return text

    def check_init(self):
        if self.i3 is None:
            self.i3 = self.init_i3()

    def init_i3(self) -> i3ipc.Connection:
        try:
            i3 = i3ipc.Connection()
            i3.on('window::focus', self.on_focus)
            i3.on('ipc_shutdown', self.on_shutdown)

            thread = Thread(target=i3.main, name='Windows i3 Thread')
            thread.daemon = True
            thread.start()
            return i3
        except FileNotFoundError:
            return None

    def on_focus(self, i3, e):
        self.state = e.container.name

    def on_shutdown(self, i3):
        self.i3 = None
        self.last_state = self.state
        self.state = None
