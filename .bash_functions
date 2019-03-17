#!/bin/bash

gi() {
    curl -sLw n https://www.gitignore.io/api/$@
}

DOTENV_BIN=$(which dotenv)
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
    for e in $($DOTENV_BIN -f "$FILENAME" list); do
        export "$e"
    done
}
