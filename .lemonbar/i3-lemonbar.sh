#!/bin/bash

PWD=$(dirname $0)

GEOMETRY="x24"

FONT="Roboto-8"
FONT_ICON="FontAwesome-8"

FOREGROUND="#D8DEE9"
BACKGROUND="#2E3440"

cd $(dirname $0)
./i3-lemonbar-output.py | lemonbar -p -g "$GEOMETRY" -f "$FONT" -f "$FONT_ICON" -F "$FOREGROUND" -B "$BACKGROUND"