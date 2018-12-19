#!/bin/bash

check_cmd() {
    command -v $1 > /dev/null 2>&1
}

alias cp="cp -i"
alias mv="mv -i"
# Sudo env hack
alias sudo="sudo "

if check_cmd trash; then
    alias rm="trash"
fi
if check_cmd playerctl; then
    alias np='echo "$(playerctl metadata artist) [$(playerctl metadata album)] - $(playerctl metadata title)"'
fi
if check_cmd google-chrome-unstable; then
    alias google-chrome='google-chrome-unstable'
fi

