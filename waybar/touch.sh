#!/bin/bash

stateFile="/tmp/touchState"

enableDevice() {
	hyprctl keyword input:touchdevice:enabled 1 > /dev/null
	echo "enabled" > "$stateFile"
	echo '{"text": " ", "class": "enabled"}'
}

disableDevice() {
	hyprctl keyword input:touchdevice:enabled 0 > /dev/null
	echo "disabled" > "$stateFile"
	echo '{"text": " ", "class": "disabled"}'
}

if [ ! -f "$stateFile" ]; then
	enableDevice
else
	if cat "$stateFile" | grep "enabled" &> /dev/null; then
		disableDevice
	else
		enableDevice
	fi
fi
