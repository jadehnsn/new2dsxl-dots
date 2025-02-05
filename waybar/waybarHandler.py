import sys
import os
import subprocess
import re

# sed "s|<opacity>|0.33|g" /home/jade/.config/waybar/sty.tmpl.css > /home/jade/.config/waybar/style.css


# Run file with arguments
# t {workspace} Toggle
# e {workspace} Enable
# d {workspace} Disable

def handleNonSpecialTransparency(opaque:bool):
	if opaque:
		os.system('sed "s|<opacity>|1|g" $HOME/.config/waybar/sty.tmpl.css > $HOME/.config/waybar/style.css')
	else:
		os.system('sed "s|<opacity>|0.25|g" $HOME/.config/waybar/sty.tmpl.css > $HOME/.config/waybar/style.css')


def updateSignal(): 
	os.system('pkill -SIGRTMIN+1 waybar')

def getCurrentSpecialWorkspace():
	x = subprocess.getoutput("hyprctl monitors | grep 'special workspace'")
	y = re.search(r'special:\s*([\w]+)', x)
	return y.group(1) if y else 'none'

def setWorkspaceHyprctl(enable:bool, workspace:str):
	current = getCurrentSpecialWorkspace()
	if enable == True:
		if current != workspace:
			os.system(f"hyprctl dispatch togglespecialworkspace {workspace} > /dev/null")
	else:
		if current == workspace:
			os.system(f"hyprctl dispatch togglespecialworkspace {workspace} > /dev/null")

def handleEnable(workspace:str):

	current = getCurrentSpecialWorkspace()

	if (current == workspace):
		return 0
	elif (current != 'none'):
		handleDisable(current)

	os.system('echo \'{"class": "enabled"}\' > /tmp/' + workspace + '.wbhwksp')
	handleNonSpecialTransparency(0)
	updateSignal()
	setWorkspaceHyprctl(1, sys.argv[2])

def handleDisable(workspace:str):

	os.system('echo \'{"class": "disabled"}\' > /tmp/' + workspace + '.wbhwksp')
	handleNonSpecialTransparency(1)
	updateSignal()
	setWorkspaceHyprctl(0, sys.argv[2])


def handleToggle(workspace:str):
	current = getCurrentSpecialWorkspace()
	if (current == workspace):
		handleDisable(workspace)
	else:
		handleEnable(workspace)

def main():

	if (str(sys.argv[1]) == 't'):
		handleToggle(sys.argv[2])

	elif (str(sys.argv[1]) == 'e'):
		handleEnable(sys.argv[2])
		
	elif (str(sys.argv[1]) == 'd'):
		handleDisable(sys.argv[2])
	

main()