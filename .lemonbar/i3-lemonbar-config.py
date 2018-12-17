from customblocks import NowPlaying, Workspaces, Windows
from datetime import datetime

SEPARATOR = '   '

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
