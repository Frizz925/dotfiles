#!/bin/bash

PWD=$(dirname $0)

GEOMETRY="x24"
UNDERLINE_WIDTH=3

FONT="Roboto-8"
FONT_ICON="FontAwesome-9"
FONT_UNICODE="SourceHanSans-8"

FOREGROUND="#D8DEE9"
BACKGROUND="#2E3440"
UNDERLINE="#D8DEE9"

cd $(dirname $0)
./i3-lemonbar-output.py | lemonbar -p -g "$GEOMETRY" -f "$FONT" -f "$FONT_ICON" -f "$FONT_UNICODE" -F "$FOREGROUND" -B "$BACKGROUND" -U "$UNDERLINE" -u $UNDERLINE_WIDTH
