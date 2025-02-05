import subprocess
import threading
import time
import os

global currentAccelOrientation
currentAccelOrientation = 0

def killHyprpaper(): os.system("killall hyprpaper")
def restartHyprpaper (): os.system("hyprpaper & disown")

def rotateScreen(direction:int):
    killHyprpaper()
    time.sleep(0.1)
    os.system("hyprctl keyword monitor eDP-1, 3840x2160@60.00000, 0x0, 1.875000, transform, " + str(direction))
    os.system("hyprctl keyword input:touchdevice:transform " + str(direction))
    os.system("hyprctl keyword input:tablet:transform " + str(direction)) 
    restartHyprpaper()

  
def getPhysicalOrientation():
    
    global currentAccelOrientation
    process = subprocess.Popen("monitor-sensor", stdout =subprocess.PIPE, text=True)
    
    while True:
        output = process.stdout.readline()
        # ANTI-Clockwise orientation with 0 being default laptop orientation
        if "Accelerometer orientation changed" in output:
            if "normal" in output:
                currentAccelOrientation = 0
            elif "right-up" in output:
                currentAccelOrientation = 3
            elif "bottom-up" in output:
                currentAccelOrientation = 2
            elif "left-up" in output:
                currentAccelOrientation = 1

physThread = threading.Thread(target=getPhysicalOrientation, args=())
physThread.start()

old = 0
while True:
    if currentAccelOrientation != old:
        rotateScreen(currentAccelOrientation)
    old = currentAccelOrientation
    time.sleep(1)
