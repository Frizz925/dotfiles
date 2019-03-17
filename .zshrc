export ZSH=$HOME/.oh-my-zsh

if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
  ZSH_THEME="cypher"
else
  export EDITOR='nvim'
  alias vim='nvim'
  ZSH_THEME="robbyrussell"
fi

plugins=(git kubectl)
source $ZSH/oh-my-zsh.sh

if [ -f ~/.bash_profile ]; then
    source ~/.bash_profile
fi
if [ -f ~/.zsh_plugins.sh ]; then
    source ~/.zsh_plugins.sh
elif [ -f ~/.zsh_plugins.txt ]; then
    if command -v antibody > /dev/null 2>&1; then
        echo "Initializing Antibody..."
        antibody bundle < ~/.zsh_plugins.txt > ~/.zsh_plugins.sh
        source ~/.zsh_plugins.sh
    fi
fi

# vim: sts=2 ts=2 sw=2

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
