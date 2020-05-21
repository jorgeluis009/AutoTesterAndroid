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

def read_device(j=1, debug=False, log_file=os.path.join('log', 'log.csv')):
    i = int(j)
    if i < 1:
        if debug:
            write_file(log_file, ['result'], {'result': 'Valor invalido, i debe ser mayor a 1 y entero'})
        raise ValueError('Valor invalido, i debe ser mayor a 0 y entero')
    if len(check_output(['adb', 'devices']).splitlines()) == 2:
        if debug:
            write_file(log_file, ['result'], {'result': 'No se encontro ningun dispositivo'})
        raise ValueError('No se encontro ningun dispositivo')
    output = check_output(['adb', 'devices']).splitlines()[i]
    serial = output.split()[0]
    if debug:
        write_file(log_file, ['result'], {'result': 'Serial = {}'.format(serial)})
        print ('Serial = {}'.format(serial))
    return serial


def read_devices(debug=False, log_file=os.path.join('log', 'log.csv')):
    s = ''
    serials = []
    output = check_output(['adb', 'devices']).splitlines()
    if len(output) == 2:
        if debug:
            write_file(log_file, ['result'], {'result': 'Device not founded'})
        raise ValueError('Device not founded')
    for i in range(1, len(output) - 1):
        serials.append(output[i].split()[0])
        if debug:
            s += 'Serial {} = {}'.format(i, serials[-1])+'-'
            print ('Serial {} = {}'.format(i, serials[-1]))
    if debug:
        write_file(log_file, ['result'], {'result': s})
    return serials


def adbCall(phone_number, serial, debug=False, log_file=os.path.join('log', 'log.csv')):
    for i in range(len(phone_number)):
        if not (phone_number[i] in keyboard_utils):
            if debug:
                write_file(log_file, ['result'], {'result': 'Numero de telefono invalido'})
            raise ValueError('Invalid number')

    if not len(phone_number):
        if debug:
            write_file(log_file, ['result'], {'result': 'Numero de telefono invalido'})
        raise ValueError('Invalid number')

    check_call(['adb', '-s', serial, 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:{}'.format(phone_number)])

    time.sleep(3)
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_ENDCALL'])
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    if debug:
        print ('Llamada realizada exitosamente a {}'.format(phone_number))
        write_file(log_file, ['result'], {'result': 'Llamada realizada exitosamente a {}'.format(phone_number)})


def adb_wifi(status, serial):
    check_call(['adb', '-s', serial, 'shell', 'svc wifi {}'.format(status_adb[status])])

# TWILIO FUNCTION
def make_twilio_call(message, toNum, fromNum):
    account_sid = twilioData['account_sid']
    auth_token = twilioData['auth_token']
    response = VoiceResponse()
    response.pause(length=10)
    response.say(message, voice='woman', language='es')
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                            twiml=response,
                            to=toNum,
                            from_=fromNum,
                            timeout=120,
                        )