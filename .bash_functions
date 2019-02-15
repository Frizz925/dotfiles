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
        _error
        _error "Usage: dc COMMAND [ARGS]"
        return 1
    fi
    for c in $(docker ps -aq); do
        docker ${@} $c
    done
}

function di() {
    if [ -z "$1" ]; then
        _error "Shorthand function for managing Docker images"
        _error
        _error "Usage: di COMMAND [ARGS]"
        return 1
    fi
    for i in $(docker images -aqf "dangling=true"); do
        docker ${@} $i
    done
}
