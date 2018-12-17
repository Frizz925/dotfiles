from i3lemonbar import Block, Scheduler
from threading import Thread

import gi
gi.require_version('Playerctl', '1.0')


class NowPlaying(Block):
    def __init__(self, scheduler: Scheduler):
        super(NowPlaying, self).__init__(scheduler)
        self.player = None
        self.loop_thread = None

        self.state = None
        self.track_url = None
        self.last_state = None
        self.last_track_url = None

    def should_update(self):
        if self.player is None:
            return True
        if self.state != self.last_state:
            return True
        if self.track_url != self.last_track_url:
            return True
        return False

    def render(self):
        from gi.repository import GLib
        try:
            self.check_init()
        except GLib.Error:
            return ''

        self.last_state = self.state
        self.last_track_url = self.track_url
        return self.render_format(self.player)

    def check_init(self):
        if self.player is None:
            self.player = self.init_player()
            self.state = self.player.props.status
        if self.loop_thread is None:
            self.loop_thread = self.init_loop()
            self.loop_thread.start()

    def init_player(self):
        from gi.repository import Playerctl
        player = Playerctl.Player()
        player.on('play', self.on_state_changed)
        player.on('pause', self.on_state_changed)
        player.on('stop', self.on_state_changed)
        player.on('exit', self.on_exit)
        player.on('metadata', self.on_metadata)
        return player

    def init_loop(self) -> Thread:
        from gi.repository import GLib
        main = GLib.MainLoop()
        thread = Thread(target=main.run)
        thread.daemon = True
        return thread

    def on_state_changed(self, player):
        self.state = player.props.status
        self.scheduler.event.set()

    def on_exit(self, player):
        self.player = None
        self.state = None

    def on_metadata(self, player, e):
        if 'xesam:url' in e.keys():
            self.track_url = e['xesam:url']

    def trigger_hook(self):
        self.hook_triggered = True

    def render_format(self, player) -> str:
        icon = self.get_icon()
        artist = player.get_artist()
        album = player.get_album()
        title = player.get_title()
        return '%s  %s [%s] - %s' % (icon, artist, album, title)

    def get_icon(self) -> str:
        state = self.state
        if state == 'Stop':
            return '\uf28d'
        if state == 'Paused':
            return '\uf04c'
        if state == 'Playing':
            return '\uf04b'
        return '\uf001'
