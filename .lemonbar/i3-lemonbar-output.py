#!/usr/bin/env python3
from i3lemonbar import Scheduler
from customblocks import NowPlaying, Workspaces
from datetime import datetime

import sys


LEFT_BLOCKS = [
    Workspaces,
]
CENTER_BLOCKS = [
    NowPlaying,
]
RIGHT_BLOCKS = [
    lambda: '\uf133  ' + datetime.now().strftime('%a, %Y-%m-%d'),
    lambda: '\uf017  ' + datetime.now().strftime('%H:%M:%S'),
]

if __name__ == '__main__':
    try:
        Scheduler(LEFT_BLOCKS, CENTER_BLOCKS, RIGHT_BLOCKS).start()
    except BrokenPipeError:
        sys.exit(1)
