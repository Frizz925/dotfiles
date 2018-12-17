from i3lemonbar import Block, Scheduler
from threading import Thread
import i3ipc


class Workspaces(Block):
    def __init__(self, scheduler: Scheduler):
        super(Workspaces, self).__init__(scheduler)
        self.i3 = None
        self.state = None
        self.last_state = None
        self.scheduler = scheduler

    def init_i3(self) -> i3ipc.Connection:
        try:
            i3 = i3ipc.Connection()
            i3.on('workspace::focus', self.on_focus)
            i3.on('ipc_shutdown', self.on_shutdown)

            thread = Thread(target=i3.main, name='Workspaces i3 Thread')
            thread.daemon = True
            thread.start()

            return i3
        except FileNotFoundError:
            return None

    def on_focus(self, i3: i3ipc.Connection, e):
        self.state = e.current.name
        self.scheduler.event.set()

    def on_shutdown(self, i3: i3ipc.Connection):
        self.i3.main_quit()
        self.i3 = None
        self.last_state = self.state
        self.state = None

    def get_focused_workspace(self):
        for ws in self.i3.get_workspaces():
            if ws.focused:
                return ws.name
        return None

    def should_update(self):
        return self.i3 is None or self.state != self.last_state

    def render(self):
        if self.i3 is None:
            self.i3 = self.init_i3()
            if self.i3 is None:
                return ''
            self.state = self.get_focused_workspace()
        if self.state is None:
            return ''

        self.last_state = self.state
        return '  '.join(map(self.format_workspace, self.i3.get_workspaces()))

    def format_workspace(self, ws):
        try:
            idx = ws.name.index(':')
            name = ws.name[idx+1:]
            if ws.focused:
                return '%%{+u}  %s  %%{-u}' % name
            else:
                return '  %s  ' % name
        except ValueError:
            return '  %s  ' % ws.name
