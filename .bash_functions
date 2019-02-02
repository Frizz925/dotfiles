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
        _error "Commands:"
        _error "  clear     Clear all containers"
        return 1
    fi
    ARG="$1"
    shift
    case "$ARG" in
        clear)
            for c in $(docker ps -aq); do
                docker rm ${@} $c
            done
            ;;
    esac 
}

function di() {
    if [ -z "$1" ]; then
        _error "Shorthand function for managing Docker images"
        _error
        _error "Usage: di COMMAND [ARGS]"
        _error "Commands:"
        _error "  clear     Clear all images"
        return 1
    fi
    ARG="$1"
    shift
    case "$ARG" in
        clear)
            for i in $(docker images -aqf "dangling=true"); do
                docker rmi ${@} $i
            done
            ;;
    esac
}
