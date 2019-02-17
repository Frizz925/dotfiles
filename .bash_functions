#!/bin/bash

gi() {
    curl -sLw n https://www.gitignore.io/api/$@
}

dotenv() {
    if [ -z "$1" ]; then
        echo "File argument required." >&2
        return 1
    fi
    if [ ! -f "$1" ]; then
        echo "File '$1' not found." >&2
        return 1
    fi
    IFS=$'\n'
    for e in $(cat "$1"); do
        export $(printf $e | xargs)
    done
}
