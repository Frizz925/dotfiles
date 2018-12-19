from customblocks import NowPlaying, Workspaces, Windows, PulseAudio
from datetime import datetime

BAR_HEIGHT = 22
UNDERLINE_HEIGHT = 3

FONT_SIZE = 8
FONT_ICON_SIZE = 9

FONT = 'Roboto'
FONT_ICON = 'FontAwesome'
FONT_UNICODE = 'SourceHanSans'
FONT_EMOJI = 'NotoColorEmoji'

FOREGROUND = "#D8DEE9"
BACKGROUND = "#2E3440"
UNDERLINE = "#D8DEE9"

SEPARATOR = '   '

LEFT_BLOCKS = [
    Workspaces,
]

CENTER_BLOCKS = [
    Windows,
]

RIGHT_BLOCKS = [
    NowPlaying,
    PulseAudio,
    lambda: '\uf133  ' + datetime.now().strftime('%a, %Y-%m-%d'),
    lambda: '\uf017  ' + datetime.now().strftime('%H:%M:%S'),
]
