if [ $UID -eq 0 ]; then NCOLOR="red"; else NCOLOR="white"; fi

export EDITOR=vim
#PROMPT='%{$fg[$NCOLOR]%}%B%n%b%{$reset_color%}:%{$fg[blue]%}%B%c/%b%{$reset_color%} $(git_prompt_info)%(!.#.$) '
#RPROMPT='[%*]'

autoload -Uz vcs_info
precmd() { 
	vcs_info
}

get_battery_capacity() {
    if [ -f /sys/class/power_supply/BAT0/capacity ]; then
        capacity=$(cat /sys/class/power_supply/BAT0/capacity)
        if [ "$capacity" -gt 40 ]; then
            echo "%{$fg[green]%}$capacity%%%{$reset_color%}"
        elif [ "$capacity" -ge 20 ]; then
            echo "%{$fg[yellow]%}$capacity%%%{$reset_color%}"
        else
            echo "%{$fg[red]%}$capacity%%%{$reset_color%}"
        fi
    else
        echo "%{$fg[red]%}N/A%{$reset_color%}"
    fi
}

get_battery_status() {
    if [ -f /sys/class/power_supply/BAT0/status ]; then
        battery_status=$(cat /sys/class/power_supply/BAT0/status)
        if [ "$battery_status" = "Charging" ]; then
            echo "+"
        else
            echo ""
        fi
    else
        echo ""
    fi
}

zstyle ':vcs_info:git:*' formats '(%F{yellow}%b%f%) '

setopt PROMPT_SUBST

PROMPT='%F{cyan}%n%f @ %F{magenta}%M%f %2~ > '
RPROMPT='${vcs_info_msg_0_}%T $(get_battery_capacity)$(get_battery_status)'

# git theming
ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}(%{$fg_no_bold[yellow]%}%B"
ZSH_THEME_GIT_PROMPT_SUFFIX="%b%{$fg_bold[blue]%})%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_CLEAN=""
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg_bold[red]%}✗"

# LS colors, made with https://geoff.greer.fm/lscolors/
export LSCOLORS='gxcxhxexfxeggdgbagacad'
export LS_COLORS='di=36:ln=32:so=37:pi=34:ex=35:bd=34;46:cd=36;43:su=36;41:sg=30;46:tw=30;42:ow=30;43'
