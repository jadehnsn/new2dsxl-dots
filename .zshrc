export ZSH="$HOME/.config/oh-my-zsh"
export EDITOR=vim

ZSH_THEME="jade"

zstyle ':omz:update' mode auto      # update automatically without asking

ENABLE_CORRECTION="true"

HIST_STAMPS="dd/mm/yyyy"

plugins=(git zsh-syntax-highlighting zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}


