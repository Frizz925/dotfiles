#!/usr/bin/env python
import io
import os
import subprocess
import sys
import signal

CWD = os.path.dirname(__file__)
CONFIG_MODULE = 'i3-lemonbar-config'
OUTPUT_MODULE = 'i3-lemonbar-output'
# The lemonbar subprocess
LEMONBAR = None
TRAP_SIGNALS = signal.SIGHUP | signal.SIGINT | signal.SIGKILL | signal.SIGTERM


def handle_signal():
    if isinstance(LEMONBAR, subprocess.Popen):
        LEMONBAR.kill()


def main():
    global LEMONBAR
    config = __import__(CONFIG_MODULE)
    scale = float(os.environ.get('WINIT_HIDPI_FACTOR', 1.0))

    bar_height = round(config.BAR_HEIGHT * scale)
    underline_height = round(config.UNDERLINE_HEIGHT * scale)

    font_size = round(config.FONT_SIZE * scale)
    font_icon_size = round(config.FONT_SIZE * scale)

    geometry = 'x%d' % bar_height

    font = '%s-%d' % (config.FONT, font_size)
    font_icon = '%s-%d' % (config.FONT_ICON, font_icon_size)
    font_unicode = '%s-%d' % (config.FONT_UNICODE, font_size)
    font_emoji = '%s-%d' % (config.FONT_EMOJI, font_size)

    foreground = config.FOREGROUND
    background = config.BACKGROUND
    underline = config.UNDERLINE

    output = __import__(OUTPUT_MODULE)
    bar_args = [
        'lemonbar', '-p',
        '-g', geometry, '-u', underline_height,
        '-f', font, '-f', font_icon,
        '-f', font_unicode, '-f', font_emoji,
        '-F', foreground, '-B', background,
        '-U', underline,
    ]
    bar_args = [str(arg) for arg in bar_args]
    lemonbar = subprocess.Popen(
        bar_args, stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stderr)
    LEMONBAR = lemonbar

    try:
        stdin = io.TextIOWrapper(lemonbar.stdin)
        output.main(stdout=stdin, stderr=sys.stderr)
    except KeyboardInterrupt:
        pass
    finally:
        lemonbar.kill()


if __name__ == '__main__':
    signal.signal(TRAP_SIGNALS, handle_signal)
    main()

# vim: ft=python ts=4 sts=4 sw=4 expandtab
