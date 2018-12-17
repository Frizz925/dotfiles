#!/bin/bash
if [ $(uname -s) = 'Linux' ]; then
    export IS_LINUX=1
fi


export GOPATH=$HOME/go

export LANGUAGE=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8
export LC_TYPE=en_US.UTF-8
export LANG=en_US.UTF-8

alias cwd='cd $(readlink $(pwd))'

# Avoid PATH duplicate
if [ -z "$ORIGINAL_PATH" ]; then
    export ORIGINAL_PATH=$PATH
fi
export PATH=$ORIGINAL_PATH
# Android stuff
if [ -d "$ANDROID_HOME" ]; then
    export PATH=$ANDROID_HOME/tools/bin:$PATH
    export PATH=$ANDROID_HOME/platform-tools:$PATH
fi
# Golang stuff
if [ -n "$GOPATH" ] && [ -d "$GOPATH" ]; then
    export PATH=$GOPATH/bin:$PATH
fi
# Ruby stuff
export PATH=$HOME/.gem/ruby/2.5.0/bin:$PATH
export PATH=/usr/lib/ruby/gems/2.5.0/bin:$PATH

if [ -d "$HOME/.local/bin" ]; then
    export PATH=$HOME/.local/bin:$PATH
fi
export PATH=/usr/local/sbin:$PATH
export PATH=/usr/local/bin:$PATH

# User specific
export PATH=$HOME/.config/composer/vendor/bin:$PATH
export PATH=$HOME/.bin:$PATH

# Python stuff
# Pipenv specific
if command -v pipenv > /dev/null 2>&1; then
    eval "$(pipenv --completion)"
    export PIPENV_VERBOSITY=-1
    export PIPENV_VENV_IN_PROJECT=1
fi

if [ -f $HOME/.bash_aliases ]; then
	source $HOME/.bash_aliases
fi
