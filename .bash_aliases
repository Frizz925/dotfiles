alias cp="cp -i"
alias mv="mv -i"
if command -v trash > /dev/null 2>&1; then
    alias rm="trash"
fi
# Sudo env hack
alias sudo="nocorrect sudo"
alias spotify="echo \"$(playerctl metadata artist) [$(playerctl metadata album)] - $(playerctl metadata title)\""
