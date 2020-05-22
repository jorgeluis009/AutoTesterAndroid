# coding=utf-8
import time
from uiautomator import Device
from src.utils.sourceData import myJson
from src.utils.sourceDataDummy import myJson2
from utils.utils import getSerial, detectDevices, adbCall, create_file, write_file
from utils.ui import uiCall, uiWifi, uiCalculator, checkForVoiceMail
from utils.utils import twilioCall
from datetime import datetime

dev = Device()
count = 0

def voiceMessage(testCase):
    twilioCall(testCase['parameters']['to'], testCase['parameters']['from'], testCase['parameters']['message'])
    time.sleep(100)
    checkForVoiceMail(dev)

for testCase in myJson2:
    now = str(datetime.now())
    try:
        print "Test Case #{} = {}".format(count+1, testCase['function'])

        if testCase["function"] == "detectDevices":
            detectDevices(True)

        elif testCase["function"] == 'read_device':
            getSerial(True)

        elif testCase['function'] == 'callADB':
            adbCall(testCase['parameters']['number_phone'])

        elif testCase['function'] == 'callUI':
            uiCall(testCase['parameters']['number_phone'], dev)

        elif testCase['function'] == 'wifiUI':
            uiWifi(int(testCase['parameters']['option']), dev)

        elif testCase['function'] == 'calculatorUI':
            uiCalculator(dev, testCase['parameters']['num_1'], testCase['parameters']['operator'],testCase['parameters']['num_1'])

        elif testCase['function'] == 'ui_voice_message':
            voiceMessage(testCase)
    except Exception as e:
        print e
    count += 1
    end = str(datetime.now())


    test_number = str(count)
    testCase['test'] = 'TC-' + test_number
    testCase['start'] = now
    testCase['end'] = end

    print testCase
    print "=================="
    # write_file(log_file, fieldnames, testCase)