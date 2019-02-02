#!/bin/bash

function _error() {
    echo ${@} >&2
}

function gi() {
    curl -L -s https://www.gitignore.io/api/$@
}

function dc() {
    if [ -z "$1" ]; then
        _error "Shorthand function for managing Docker containers"
        _error "Usage: dc clear <...args>"
        return 1
    fi
    ARG="$1"
    shift
    case "$ARG" in
        clear)
            CONTAINERS=$(docker ps -aq)
            if [ -z "$CONTAINERS" ]; then
                _error "No containers to remove"
                return 1
            fi
            docker rm ${@} "$CONTAINERS"
            ;;
    esac 
}
