if [ -f $HOME/.xsessionrc ]; then
    source $HOME/.xsessionrc
fi
if [ -f $HOME/.Xresources ]; then
    xrdb $HOME/.Xresources
fi
i3

# vim: ft=sh
