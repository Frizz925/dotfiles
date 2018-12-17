#!/bin/bash

COMMAND="./i3-lemonbar.sh"

cleanup() {
    pkill -9 -f i3-lemonbar > /dev/null 2>&1
    pkill -9 -f lemonbar > /dev/null 2>&1
}
trap cleanup EXIT

cd $(dirname $0)
$COMMAND &
PID=$!
inotifywait -me close_write . | \
    while read -r directory event filename; do
        if [[ $filename != *"i3-lemonbar"* ]]; then
            continue
        fi
        kill -9 $PID
        killall lemonbar
        $COMMAND &
        PID=$!
    done

