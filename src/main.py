# coding=utf-8
import time
from uiautomator import Device
import os
from src.utils.sourceData import myJson
from src.utils.sourceDataDummy import myJson2
from utils.utils import read_device, read_devices, adbCall, create_file, write_file
from utils.ui import adb_ui_call, adb_ui_wifi, adb_ui_calculator, adb_ui_voice_message
from utils.utils import make_twilio_call
from datetime import datetime

dev = Device()
def test_read_devices(case_data, log_result):
    read_devices(debug=True, log_file=log_result)


def test_read_device(case_data, log_result):
    read_device(case_data['parameters']['device_id'], debug=True, log_file=log_result)


def test_adb_call(case_data, log_result):
    serial = read_device(case_data['parameters']['device_id'], debug=False)
    adbCall(case_data['parameters']['number_phone'], serial,
             debug=True, log_file=log_result)


def test_adb_ui_call(case_data, log_result):
    serial = read_device(case_data['parameters']['device_id'], debug=False)
    device = Device(serial)
    adb_ui_call(case_data['parameters']['number_phone'], float(case_data['parameters']['seconds']), device,
                debug=True, log_file=log_result)


def test_adb_ui_wifi(case_data, log_result):
    serial = read_device(case_data['parameters']['device_id'], debug=False)
    device = Device(serial)
    adb_ui_wifi(int(case_data['parameters']['status']), device,
                debug=True, log_file=log_result)


def test_adb_ui_calculator(case_data, log_result):
    serial = read_device(case_data['parameters']['device_id'], debug=False)
    device = Device(serial)
    adb_ui_calculator(case_data['parameters']['operand1'], case_data['parameters']['operator'],
                      case_data['parameters']['operand2'], device,
                      debug=True, log_file=log_result)


def test_adb_ui_voice_message(case_data):
    serial = read_device(case_data['parameters']['device_id'], debug=False)
    device = Device(serial)

    make_twilio_call(case_data['parameters']['message'], case_data['parameters']['to'], case_data['parameters']['from'])
    # time.sleep(120)
    # adb_ui_voice_message(device, debug=True, log_file=log_result)

# log_file = os.path.join('log', str(datetime.now().strftime("%d%m%Y")) + '.csv')
# log_result = log_file[0:-4] + '_data.csv'
# print log_result
# create_file(log_result, ['result'])
# fieldnames = ['test', 'function', 'txt', 'isAuto', 'parameters', 'expected result', 'begin', 'end']
# create_file(log_file, fieldnames)
i = 0

for testCase in myJson2:
    now = str(datetime.now())
    try:
        print "Test Case = {}".format(testCase['function'])

        if testCase['function'] == 'read_devices2':
            read_devices(flag=True)
        elif testCase['function'] == 'read_device':
            test_read_device(testCase)
        elif testCase['function'] == 'adb_call2':
            test_adb_call(testCase)
        elif testCase['function'] == 'adb_ui_call':
            test_adb_ui_call(testCase)
        elif testCase['function'] == 'adb_ui_wifi':
            test_adb_ui_wifi(testCase)
        elif testCase['function'] == 'adb_ui_calculator':
            test_adb_ui_calculator(testCase)
        elif testCase['function'] == 'ui_voice_message':
            test_adb_ui_voice_message(testCase)
    except Exception as ex:
        print ex

    end = str(datetime.now())
    i += 1
    test_number = str(i)
    while len(test_number) < 3:
        test_number = '0' + test_number
    testCase['test'] = 'TC' + test_number
    testCase['begin'] = now
    testCase['end'] = end
    print testCase
    print "=================="
    # write_file(log_file, fieldnames, testCase)