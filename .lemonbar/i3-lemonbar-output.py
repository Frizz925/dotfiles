#!/usr/bin/env python3
from typing import List
from threading import Thread
from inspect import isclass
from datetime import datetime

import gi
import time
import sys

gi.require_version('Playerctl', '1.0')


class Block(object):
    def __init__(self, renderer=None):
        self.renderer = renderer

    def should_update(self) -> bool:
        return True

    def render(self) -> str:
        if isinstance(self.renderer, str):
            return self.renderer
        if callable(self.renderer):
            return self.renderer()
        return ''


class BlockRenderer(object):
    def __init__(self, blocks: List, separator='  '):
        self.blocks = self.delegate_blocks(blocks)
        self.separator = separator
        self.render_map = {}

    def delegate_blocks(self, blocks: List):
        return list(map(self.delegate_renderer, blocks))

    def delegate_renderer(self, renderer):
        if isclass(renderer):
            renderer = renderer()
        if isinstance(renderer, Block):
            return renderer
        return Block(renderer)

    def render(self) -> str:
        separator = self.render_separator()
        return separator.join(map(self.render_block, self.blocks))

    def render_separator(self) -> str:
        return self.separator

    def render_block(self, block: Block) -> str:
        if block in self.render_map and not block.should_update():
            return self.render_map[block]
        rendered = block.render()
        self.render_map[block] = rendered
        return rendered

    def block_to_str(self, block) -> str:
        if isclass(block):
            block = block()
        if callable(block):
            return block()
        if isinstance(block, Block):
            return block.render()
        if isinstance(block, str):
            return block
        raise TypeError('Unknown block type of %s' % type(block))


class Scheduler(object):
    def __init__(self, left_blocks=[], center_blocks=[], right_blocks=[]):
        self.left_renderer = BlockRenderer(left_blocks)
        self.center_renderer = BlockRenderer(center_blocks)
        self.right_renderer = BlockRenderer(right_blocks)
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.run()
            self.sleep()

    def run(self):
        sys.stdout.write('%%{l} %s %%{l}' % self.left_renderer.render())
        sys.stdout.write('%%{c} %s %%{c}' % self.center_renderer.render())
        sys.stdout.write('%%{r} %s %%{r}' % self.right_renderer.render())
        sys.stdout.write('\n')
        sys.stdout.flush()

    def sleep(self):
        time.sleep(1)


class NowPlaying(Block):
    def __init__(self):
        super(Block, self).__init__()
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


LEFT_BLOCKS = []
CENTER_BLOCKS = [
    NowPlaying,
]
RIGHT_BLOCKS = [
    lambda: '\uf133  ' + datetime.now().strftime('%a, %Y-%m-%d'),
    lambda: '\uf017  ' + datetime.now().strftime('%H:%M:%S'),
]

if __name__ == '__main__':
    Scheduler(LEFT_BLOCKS, CENTER_BLOCKS, RIGHT_BLOCKS).start()
