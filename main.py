from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz
import os

num = input("Enter number to call; ")
os.system("adb shell am start -a android.intent.action.CALL -d tel:"+str(num))