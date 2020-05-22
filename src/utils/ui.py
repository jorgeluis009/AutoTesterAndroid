# coding=utf-8
from subprocess import check_call, check_output
from uiautomator import Device
import os
import time
from AuxUtils import keyboard_utils, calculatorUI, optionsUI, operators
from utils import write_file

def goHome(dev):
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

def clickNumToCall(n,dev):
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

def uiCall(phone_number, device):
    goHome(device)
    print "home"
    myClick(device(description="Phone"))
    print 'Phone clicked'
    myLongClick(device(descriptionContains="Delete"))
    print 'deleting'
    clickNumToCall(phone_number,device)
    myClick(device(descriptionContains="Call"))
    print "Calling..."


def uiWifi(option, dev):
    if not (option in optionsUI):
        raise ValueError('Invalid option')

    x = optionsUI[option]
    y = optionsUI[option^1]

    goHome(dev)
    dev.swipe(500, 1500, 500, 500, 30)
    myClick(dev(text="Settings"))
    myClick(dev(text="Connections"))
    myClick(dev(text="Wi-Fi"))

    if dev(text='Wi-Fi, {}'.format(x), className='android.widget.Switch').exists:
        print "Wi-fi is {}".format(x)
        dev(text='Wi-Fi, {}'.format(x), className='android.widget.Switch').click()

        if dev(text='Wi-Fi, {}'.format(y), className='android.widget.Switch').exists:
            print ("Wi-fi turned {}".format(y))
    else:
        goHome(dev)
        raise ValueError("Wi-fi is {0} already, not action was taken".format(y))
    goHome(dev)

def isInteger(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def isValidNumber(n):
    n = n.split(".")
    if (len(n) > 2):
        return False
    for i in n:
        if not isInteger(i):
            return False
    return True

def uiCalculator(dev, num1, operator, num2):
    if not (operator in operators):
        # if debug:
        #     write_file(log_file, ['result'], {'result': 'Operador invalido'})
        raise ValueError('Invalid operator')
    if not isValidNumber(num1) or not isValidNumber(num2):
        raise ValueError('Values are not valid')
    else:
        isNegative = False

        goHome(dev)
        dev.swipe(500, 1500, 500, 500, 30)
        myClick(dev(text="Calculator"))
        myClick(dev(text="C"))

        a = num1
        b = num2

        for i in range(len(a)):
            if a[i] == '-':
                isNegative = True
                myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_parenthesis"))
                myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_sub"))
            else:
                myClick(dev(text=a[i], className='android.widget.Button'))

        if isNegative:
            myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_parenthesis"))

        # Click operator
        myClick(dev(resourceId = "com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}".format(calculatorUI[operator])))

        isNegative = False
        for i in range(len(b)):
            if b[i] == '-':
                isNegative = True
                myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_parenthesis"))
                myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_sub"))
            else:
                myClick(dev(text=b[i], className='android.widget.Button'))
        if isNegative:
            myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_parenthesis"))

        #Click equal
        myClick(dev(resourceId="com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal"))


def checkForVoiceMail(dev):
    title = "new voicemail"
    dev.open.notification()
    if dev(text='Call settings', className='android.widget.TextView').exists:
        str = dev(resourceId='android:id/title').text
        if title in str:
            print "Voicemail found"
    else:
        print "No voicemails here"

    goHome(dev)
