#!/bin/bash

COMMAND="./i3-lemonbar.sh"

cd $(dirname $0)

$COMMAND &
inotifywait -me close_write . | \
    while read -r directory event filename; do
        if [[ $filename != *"i3-lemonbar"* ]]; then
            continue
        fi
        killall lemonbar
        $COMMAND &
    done

