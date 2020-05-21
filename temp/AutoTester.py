# coding=utf-8
import time
from uiautomator import Device
import Manager as man
import os
from src.utils.sourceData import myJson

dev = Device()
operations = ['+','−','×','÷']

def goHome():
    dev.press.home()
    time.sleep(1)

def myClick(button):
    if (button.count != 0):
        button.click()
        time.sleep(1)

def myLongClick(button):
    if(button.count != 0):
        button.long_click()
        time.sleep(1)

def clickNum(n):
    if(n[0] == "-"):
        myClick(dev(text="( )"))
        myClick(dev(text="−"))
        for i in n[1:]:
            if(i == "."):
                myClick(dev(text=i))
            else:
                myClick(dev(description=i))
        myClick(dev(text="( )"))
    else:
        for i in n:
            if (i == "."):
                myClick(dev(text=i))
            else:
                myClick(dev(description=i))

def clickNumToCall(n):
    print n
    if(n[0] == "+"):
        myLongClick(dev(description="0"))
        n = n[1:]
    elif (n[0] == "#"):
        myClick(dev(text="#"))
        n = n[1:]
    elif (n[0] == "*"):
        myClick(dev(text="∗"))
        n = n[1:]
    for i in n:
        myClick(dev(description=i))

def startCalculator():
    op = 0
    n1 = man.inputNum()
    while(op <=0 or op >+5):
        print "1)+"
        print "2)-"
        print "3)x"
        print "4)/"
        op = int(input("Choose operation: "))
    n2 = man.inputNum()
    goHome()
    print myJson[0]['function']
    dev.swipe(500, 1500, 500, 500, 30)

    # click Calculator btn
    myClick(dev(text=man.btns[0]))

    # click delete "C" btn
    myClick(dev(text=man.btns[1]))

    clickNum(n1)
    myClick(dev(text=operations[op-1]))
    clickNum(n2)
    myClick(dev(text="="))
    print myJson[0]['expected_txt']

def toggleWifi():
    print myJson[3]['function']
    print myJson[3]['txt']
    if (dev(text="On")):
        myClick(dev(text="On"))
    else:
        myClick(dev(text="Off"))
    print myJson[3]['expected_txt']

def interactWifi():
    goHome()
    dev.swipe(500, 1500, 500, 500, 30)
    myClick(dev(text="Settings"))
    myClick(dev(text="Connections"))
    myClick(dev(text="Wi-Fi"))
    toggleWifi()
    goHome()

def makeACallADB():
    num = input("Enter number to call; ")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:" + str(num))


def makeACall():
    goHome()
    myClick(dev(description="Phone"))
    print 'Phone clicked'
    myLongClick(dev(descriptionContains="Delete"))
    print 'deleting'

    num = str(raw_input("enter number = "))
    print "number entered" + num
    clickNumToCall(num)
    myClick(dev(descriptionContains="Call"))
    print "Calling..."

print("Detecting devices...\n")
man.identifyDevice()
print ("==========================================")
print("Choose action to perform\n")
selection = input("1)Use calculator\n2)Make a Call (Using UiAutomator)\n3)Make a Call (Using ADB)\n4)Toggle Wi-Fi\n5)Identify Devices\nOption: ")

if selection == 1: #Use Calculator
    startCalculator()
elif selection == 2: # Call UiAuto
    makeACall()
elif selection == 3: # Call ADB
    makeACallADB()
elif selection == 4: # Wifi
    interactWifi()
else:
    print "not valid"