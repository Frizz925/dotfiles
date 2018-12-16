if [ -f $HOME/.xsessionrc ]; then
    source $HOME/.xsessionrc
fi
if [ -f $HOME/.Xresources ]; then
    xrdb $HOME/.Xresources
fi
if command -v gnome-keyring-daemon > /dev/null 2>&1; then
    eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh,gpg)
    export SSH_AUTH_SOCK
    dbus-update-activation-environment --systemd DISPLAY
fi
i3

# vim: ft=sh
