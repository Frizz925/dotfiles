from i3lemonbar import Block
from i3lemonbar.containers import inject
from i3lemonbar.i3wrapper import i3Wrapper
import i3ipc


@inject(i3Wrapper)
class Workspaces(Block):
    def __init__(self, i3_wrapper: i3Wrapper):
        self.i3_wrapper = i3_wrapper
        self.state = None
        self.last_state = None

        self.i3_wrapper.on('workspace::focus', self.on_focus)
        self.i3_wrapper.on('ipc_shutdown', self.on_shutdown)

    def on_focus(self, i3: i3ipc.Connection, e):
        self.state = e.current.name

    def on_shutdown(self, i3: i3ipc.Connection):
        self.last_state = self.state
        self.state = None

    def should_update(self):
        return not self.i3_wrapper.connected() or self.state != self.last_state

    def render(self):
        if not self.i3_wrapper.connected():
            return ''
        self.last_state = self.state
        if self.state is None:
            self.state = self.get_focused_workspace()
        i3 = self.i3_wrapper.i3
        workspaces = i3.get_workspaces()
        return '  '.join(map(self.format_workspace, workspaces))

    def get_focused_workspace(self):
        if not self.i3_wrapper.connected():
            return None
        i3 = self.i3_wrapper.i3
        for ws in i3.get_workspaces():
            if ws.focused:
                return ws.name
        return None

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
