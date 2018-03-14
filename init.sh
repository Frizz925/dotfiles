#!/bin/sh

GITHUB_URL="https://github.com"
ZSH_PLUGINS=".oh-my-zsh/custom/plugins"

git clone $GITHUB_URL/zsh-users/zsh-autosuggestions $ZSH_PLUGINS/zsh-autosuggestions
git clone $GITHUB_URL/zsh-users/zsh-syntax-highlighting $ZSH_PLUGINS/zsh-syntax-highlighting
git clone $GITHUB_URL/zsh-users/zsh-history-substring-search $ZSH_PLUGINS/zsh-history-substring-search

