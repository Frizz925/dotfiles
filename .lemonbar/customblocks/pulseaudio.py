from i3lemonbar import Block, Scheduler
from i3lemonbar.containers import inject
from threading import Thread
import pulsectl


@inject(Scheduler)
class PulseAudio(Block):
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler
        self.pulse = None
        self.pulse_thread = None
        self.state = None
        self.last_state = None
        self.hook_triggered = False

    def should_update(self) -> bool:
        return self.hook_triggered or \
            self.pulse is None or \
            self.state != self.last_state

    def render(self) -> str:
        self.check_init()
        if self.hook_triggered:
            self.pulse.event_listen_stop()
            self.pulse_thread.join()
            self.state = self.init_state(self.pulse)
            self.pulse_thread = self.init_pulse_thread(self.pulse)
            self.hook_triggered = False
        self.last_state = self.state
        return self.state

    def check_init(self):
        if self.pulse is None:
            self.pulse = self.init_pulse()
        if self.state is None:
            self.state = self.init_state(self.pulse)
        if self.pulse_thread is None:
            self.pulse_thread = self.init_pulse_thread(self.pulse)

    def init_pulse(self):
        pulse = pulsectl.Pulse()
        pulse.event_mask_set('all')
        pulse.event_callback_set(self.update_state)
        return pulse

    def init_state(self, pulse: pulsectl.Pulse):
        name = pulse.server_info().default_sink_name
        sink = filter(lambda x: x.name == name, pulse.sink_list())
        sink = list(sink).pop()
        if sink is None or sink.mute:
            volume = 0
        else:
            volume = round(sink.volume.value_flat * 100)

        icon = '\uf026'
        if volume > 50:
            icon = '\uf028'
        elif volume > 0:
            icon = '\uf027'
        return '%s  %d%%' % (icon, volume)

    def init_pulse_thread(self, pulse: pulsectl.Pulse):
        thread = Thread(target=pulse.event_listen, name='PulseAudio Thread')
        thread.daemon = True
        thread.start()
        return thread

    def update_state(self, e):
        # TODO: Remove workaround and use asyncio/twisted
        self.hook_triggered = True
        self.scheduler.event.set()
