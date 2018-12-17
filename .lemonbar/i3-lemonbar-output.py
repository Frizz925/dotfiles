#!/usr/bin/env python3
from i3lemonbar import Scheduler
from customblocks import NowPlaying, Workspaces, Windows
from datetime import datetime

LEFT_BLOCKS = [
    Workspaces,
]
CENTER_BLOCKS = [
    Windows,
]
RIGHT_BLOCKS = [
    NowPlaying,
    lambda: '\uf133  ' + datetime.now().strftime('%a, %Y-%m-%d'),
    lambda: '\uf017  ' + datetime.now().strftime('%H:%M:%S'),
]
SEPARATOR = '   '

if __name__ == '__main__':
    Scheduler(LEFT_BLOCKS, CENTER_BLOCKS, RIGHT_BLOCKS, SEPARATOR).start()
