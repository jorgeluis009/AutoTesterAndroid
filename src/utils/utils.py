import csv
import time
import os
from src.utils.dataKeys import twilioData
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from subprocess import check_call, check_output
from src.utils.AuxUtils import status_adb, keyboard_utils

def create_file(file_name, headers):
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

def write_file(file_name, headers, row):
    with open(file_name, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(row)

def getSerial(testing=False):
    output = check_output(['adb', 'devices']).splitlines()[1]
    serial = output.split()[0]
    if testing:
        print "Serial Number = {}".format(serial)
    return serial


def detectDevices(testing):
    serialNums = []
    command = check_output(['adb', 'devices'])
    command = command.splitlines()
    size = len(command) - 1

    if size+1 == 2:
        raise ValueError('Device not found')

    for i in range(1, size):
        serialNums.append(command[i].split()[0])

        if testing:
            print 'Serial Number {} = #{}'.format(i, serialNums[-1])
    return serialNums

def validateNumber(num):
    if not len(num):
        return False
    for i in range(len(num)):
        if not (num[i] in keyboard_utils):
            return False
    return True

def adbCall(num):
    if(validateNumber(num)):
        check_call(['adb', 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:{}'.format(num)])
        time.sleep(3)
        check_call(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENDCALL'])
        check_call(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
        print ('Number called = {}'.format(num))
    else:
        raise ValueError('Invalid number')

def adb_wifi(status, serial):
    check_call(['adb', '-s', serial, 'shell', 'svc wifi {}'.format(status_adb[status])])

# TWILIO FUNCTION
def twilioCall(toNum, fromNum, message):
    account_sid = twilioData[0]['account_sid']
    auth_token = twilioData[0]['auth_token']
    response = VoiceResponse()
    response.say(message, voice='woman', language='es')
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                                # twiml='<Response>'
                                #       '<Say voice="alice">Thank you george, hello everyone</Say>'
                                #       '</Response>',
                                twiml=response,
                                to=toNum,
                                from_=fromNum,

                                machine_detection='DetectMessageEnd'
                         )
