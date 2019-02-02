#!/bin/zsh
check_command() {
    command -v $1 > /dev/null 2>&1
}

if [ -f $HOME/.bash_profile ]; then
    source $HOME/.bash_profile
fi
if [ -f $HOME/.vg.zsh ]; then
    source $HOME/.vg.zsh
fi
export ZSH=$HOME/.oh-my-zsh

if [[ -n $SSH_CONNECTION ]]; then
    ZSH_THEME='cypher'
    export EDITOR='vim'
else
    ZSH_THEME='robbyrussell'
    export EDITOR='nvim'
    alias vim='nvim'
fi

if check_command antibody && [ -f $HOME/.zsh_plugins.txt ]; then
    if [ ! -f $HOME/.zsh_plugins.sh ]; then
        echo "Initializing antibody"
        antibody bundle < $HOME/.zsh_plugins.txt > $HOME/.zsh_plugins.sh
    fi
    source $HOME/.zsh_plugins.sh
fi

#plugins=(git heroku pip docker composer virtualenv node npm yarn)
source $ZSH/oh-my-zsh.sh

