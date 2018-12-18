from i3lemonbar import Block
from i3lemonbar.containers import inject
from i3lemonbar.i3wrapper import i3Wrapper
import i3ipc


@inject(i3Wrapper)
class Workspaces(Block):
    workspace_titles = {
        '1': '\uf268  web',
        '2': '\uf121  code',
        '3': '\uf120  term',
        '4': '\uf086  chat',
        '5': '\uf1bc  spotify',
        '6': '\uf2d0  misc',
        '7': '\uf2d0  misc',
        '8': '\uf2d0  misc',
        '9': '\uf2d0  misc',
        '10': '\uf2d0  misc',
    }

    def __init__(self, i3_wrapper: i3Wrapper):
        self.i3_wrapper = i3_wrapper
        self.state = None
        self.last_state = None

        self.i3_wrapper.on('workspace::init', self.on_state_changed)
        self.i3_wrapper.on('workspace::focus', self.on_state_changed)
        self.i3_wrapper.on('workspace::move', self.on_state_changed)
        self.i3_wrapper.on('workspace::rename', self.on_state_changed)
        self.i3_wrapper.on('workspace::reload', self.on_state_changed)
        self.i3_wrapper.on('workspace::urgent', self.on_state_changed)
        self.i3_wrapper.on('ipc_shutdown', self.on_shutdown)

    def on_state_changed(self, i3: i3ipc.Connection, e):
        if e.current is None:
            return
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
        name = ws.name
        try:
            idx = name.index(':')
            name = name[idx+1:]
        except ValueError:
            pass
        try:
            name = self.workspace_titles[name]
        except KeyError:
            pass
        if ws.focused:
            return '%%{+u}  %s  %%{-u}' % name
        elif ws.urgent:
            return '%%{+u}%%{R}  %s  %%{R}%%{-u}' % name
        else:
            return '  %s  ' % name
