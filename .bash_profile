#!/bin/bash
if [ $(uname -s) = 'Darwin' ]; then
    export IS_OSX=1
fi

export GOPATH=$HOME/go

export LANGUAGE=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8
export LC_TYPE=en_US.UTF-8
export LANG=en_US.UTF-8

alias cwd='cd $(readlink $(pwd))'

# macOS specific
if [ -n "$IS_OSX" ]; then
    export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
    export ANDROID_HOME=/usr/local/lib/android
    export HOMEBREW_NO_AUTO_UPDATE=1
fi

# Avoid PATH duplicate
if [ -z "$ORIGINAL_PATH" ]; then
    export ORIGINAL_PATH=$PATH
fi
export PATH=$ORIGINAL_PATH
# macOS specific
if [ -n "$IS_OSX" ]; then
    export PATH=/usr/local/opt/openssl/bin:$PATH
fi
# Android stuff
if [ -d "$ANDROID_HOME" ]; then
    export PATH=$ANDROID_HOME/tools/bin:$PATH
    export PATH=$ANDROID_HOME/platform-tools:$PATH
fi
export PATH=/usr/local/sbin:$PATH
export PATH=/usr/local/bin:$PATH

# User specific
export PATH=$HOME/.composer/vendor/bin:$PATH
export PATH=$HOME/.bin:$PATH
# macOS specific
if [ -n "$IS_OSX" ]; then
    export PATH=$HOME/Library/Python/3.7/bin:$PATH
fi

# Python stuff
# Pipenv specific
if command -v pipenv > /dev/null 2>&1; then
    eval "$(pipenv --completion)"
    export PIPENV_VERBOSITY=-1
fi
