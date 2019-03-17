#!/bin/zsh

export GOPATH=~/go
export PATH=$GOPATH/bin:$HOME/.local/bin:$PATH

if [ -f ~/.bash_aliases ]; then
    source ~/.bash_aliases
fi
if [ -f ~/.bash_functions ]; then
    source ~/.bash_functions
fi
