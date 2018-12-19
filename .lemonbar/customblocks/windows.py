from i3lemonbar import Block
from i3lemonbar.containers import inject
from i3lemonbar.i3wrapper import i3Wrapper


@inject(i3Wrapper)
class Windows(Block):
    def __init__(self, i3_wrapper: i3Wrapper):
        self.i3_wrapper = i3_wrapper
        self.state = None
        self.last_state = None

        self.i3_wrapper.on('window::new', self.on_update)
        self.i3_wrapper.on('window::close', self.on_update)
        self.i3_wrapper.on('window::focus', self.on_update)
        self.i3_wrapper.on('window::title', self.on_update)
        self.i3_wrapper.on('ipc_shutdown', self.on_shutdown)

    def should_update(self) -> bool:
        return not self.i3_wrapper.connected() or self.state != self.last_state

    def render(self) -> str:
        if not self.i3_wrapper.connected():
            return ''
        self.last_state = self.state
        if self.state is None:
            i3 = self.i3_wrapper.i3
            focused = i3.get_tree().find_focused()
            self.state = focused
        return self.format(self.state)

    def format(self, con) -> str:
        return con.name

    def check_init(self):
        if self.i3 is None:
            self.i3 = self.init_i3()

    def on_update(self, i3, e):
        if e.change == 'close':
            self.state = None
        else:
            self.state = e.container

    def on_shutdown(self, i3):
        self.last_state = self.state
        self.state = None
