from i3lemonbar import Block, Scheduler
from i3lemonbar.i3wrapper import i3Wrapper
from i3lemonbar.containers import inject


@inject(Scheduler, i3Wrapper)
class Bindings(Block):
    def __init__(self, scheduler: Scheduler, i3_wrapper: i3Wrapper):
        self.scheduler = scheduler
        self.i3_wrapper = i3_wrapper
        self.current_mode = None

        self.i3_wrapper.on('mode', self.on_mode_change)

    def on_mode_change(self, i3, e):
        if e.change != 'default':
            self.current_mode = e.change
        else:
            self.current_mode = None

    def render(self):
        if self.current_mode is None:
            return ''
        return '%%{R}%%{+u}  %s  %%{-u}%%{R}' % self.current_mode
