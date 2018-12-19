#!/bin/zsh

check_command() {
  command -v $1 > /dev/null 2>&1
}

if [ -f $HOME/.bash_profile ]; then
  source $HOME/.bash_profile
fi

if [ -f $HOME/.zsh_plugins.sh ]; then
  source $HOME/.zsh_plugins.sh
elif check_command antibody && [ -f $HOME/.zsh_plugins.txt ]; then
  echo "Initializing antibody"
  antibody bundle < $HOME/.zsh_plugins.txt > $HOME/.zsh_plugins.sh
fi

if [[ -n $SSH_CONNECTION ]]; then
  ZSH_THEME='fishy'
  export EDITOR='vim'
else
  ZSH_THEME='robbyrussell'
  export EDITOR='nvim'
  alias vim='nvim'
fi

export ZSH=$HOME/.oh-my-zsh
plugins=(git)
source $ZSH/oh-my-zsh.sh

# vim: ts=2 sts=2 sw=2

