import time
import os
from uiautomator import Device

def goHome():
    while (dev.press.home()):
        time.sleep(1)

def NiceClick(button):
    if(button.count != 0):
        button.click()
        time.sleep(1)

def NiceLongClick(button):
    if(button.count != 0):
        button.long_click()
        time.sleep(1)

def toggleWifi():
    if(dev(text="On")):
        NiceClick(dev(text="On"))
    else:
        NiceClick(dev(text="Off"))

dev = Device()



goHome()
dev.swipe(500,1500,500,500,30)
NiceClick(dev(text="Settings"))
NiceClick(dev(text="Connections"))
NiceClick(dev(text="Wi-Fi"))
toggleWifi()
goHome()