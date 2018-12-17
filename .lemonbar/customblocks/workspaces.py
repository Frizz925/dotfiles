from i3lemonbar import Block, Scheduler
from threading import Thread
import i3ipc


class Workspaces(Block):
    def __init__(self, scheduler: Scheduler):
        super(Workspaces, self).__init__(scheduler)
        self.i3 = self.init_i3()
        self.i3_thread = None
        self.state = self.get_focused_workspace()
        self.last_state = None
        self.scheduler = scheduler

    def init_i3(self) -> i3ipc.Connection:
        i3 = i3ipc.Connection()
        i3.on('workspace::focus', self.update_state)
        return i3

    def init_thread(self, i3: i3ipc.Connection):
        thread = Thread(target=i3.main)
        thread.daemon = True
        return thread

    def update_state(self, i3: i3ipc.Connection, e):
        self.state = e.current.name
        self.scheduler.set()

    def get_focused_workspace(self):
        for ws in self.i3.get_workspaces():
            if ws.focused:
                return ws.name
        return None

    def should_update(self):
        return self.state != self.last_state

    def render(self):
        if self.i3_thread is None:
            self.i3_thread = self.init_thread(self.i3)
            self.i3_thread.start()
        if self.state is None:
            return ''

        self.last_state = self.state
        return self.state
