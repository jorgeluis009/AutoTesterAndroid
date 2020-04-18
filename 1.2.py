from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz
import os

def NiceClick(button):
    if(button.count != 0):
        button.click()
        time.sleep(1)

def NiceLongClick(button):
    if(button.count != 0):
        button.long_click()
        time.sleep(1)

dev = Device()

while(dev.press.home()):
    time.sleep(1)
NiceClick(dev(description="Phone"))

NiceLongClick(dev(descriptionContains="Delete"))
time.sleep(2)

num = str(input("enter number = "))
for i in num:
    dev(description=i).click()

NiceClick(dev(descriptionContains="Call"))

