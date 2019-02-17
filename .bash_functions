#!/bin/bash

gi() {
    curl -sLw n https://www.gitignore.io/api/$@
}

dotenv() {
    FILENAME="$1"
    if [ -z "$FILENAME" ]; then
        FILENAME=".env"
    fi
    if [ ! -f "$FILENAME" ]; then
        echo "File '$FILENAME' not found." >&2
        return 1
    fi
    IFS=$'\n'
    for e in $(cat "$FILENAME"); do
        export $(printf $e | xargs)
    done
}
