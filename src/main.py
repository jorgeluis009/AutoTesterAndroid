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


def test_adb_ui_voice_message(case_data, log_result):
    serial = read_device(case_data['parameters']['device_id'], debug=False)
    device = Device(serial)

    make_twilio_call(case_data['parameters']['message'], case_data['parameters']['to'], case_data['parameters']['from'])
    # time.sleep(120)
    # adb_ui_voice_message(device, debug=True, log_file=log_result)

log_file = os.path.join('log', str(datetime.now().strftime("%d%m%Y")) + '.csv')
log_result = log_file[0:-4] + '_data.csv'
print log_result
create_file(log_result, ['result'])
fieldnames = ['test', 'function', 'txt', 'isAuto', 'parameters', 'expected result', 'begin', 'end']
create_file(log_file, fieldnames)
i = 0

for case in myJson2:
        begin = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        if case['isAuto'] == 'True':
            try:
                print i
                print case['function']
                if case['function'] == 'read_devices':
                    test_read_devices(case, log_result)
                elif case['function'] == 'read_device':
                    test_read_device(case, log_result)
                elif case['function'] == 'adb_call':
                    test_adb_call(case, log_result)
                elif case['function'] == 'adb_ui_call':
                    test_adb_ui_call(case, log_result)
                elif case['function'] == 'adb_ui_wifi':
                    test_adb_ui_wifi(case, log_result)
                elif case['function'] == 'adb_ui_calculator':
                    test_adb_ui_calculator(case, log_result)
                elif case['function'] == 'ui_voice_message':
                    test_adb_ui_voice_message(case, log_result)
            except Exception as ex:
                print ex
        else:
            write_file(log_result, ['result'], {'result': 'NA'})
        end = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        i += 1
        test_number = str(i)
        while len(test_number) < 3:
            test_number = '0' + test_number
        case['test'] = 'TC' + test_number
        case['begin'] = begin
        case['end'] = end
        write_file(log_file, fieldnames, case)