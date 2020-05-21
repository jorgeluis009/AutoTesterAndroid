#My JSON
myJson = [
    # ===  identify Devices functions ===
    {#TC 1
        'function': 'read_devices',
        'isAuto': 'False',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
        'parameters': {}
    },
    {#TC 2
        'function': 'read_devices',
        'isAuto': 'True',
        'txt': 'Un dispositivo conectado',
        'expected result': 'Serial 1 = R28M30VCACV-',
        'parameters': {}
    },
    {#TC 3
        'function': 'read_devices',
        'isAuto': 'False',
        'txt': 'Dos o mas dispositivos conectados',
        'expected result': '?',
        'parameters': {}
    },
    {#TC 4
        'function': 'read_device',
        'isAuto': 'True',
        'txt': 'Un dispositivo conectado',
        'expected result': 'Serial = R28M410479V',
        'parameters': {
            'device_id': '1'
        }
    },
    {#TC 5
        'function': 'read_device',
        'isAuto': 'True',
        'txt': 'Un dispositivo conectado',
        'expected result': 'list index out of range',
        'parameters': {
            'device_id': '10'
        }
    },
    {#TC 6
        'function': 'read_device',
        'isAuto': 'False',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
        'parameters': {
            'device_id': '10'
        }
    },
    # === WIFI TC ===
    {#TC 7
        'function': 'adb_ui_wifi',
        'isAuto': 'True',
        'txt': 'Disable Wifi whit Wifi ON',
        'expected result': 'Wifi turned Off',
        'parameters': {
            'device_id': '1',
            'status': '0',
        }
    },
    {#TC 8
        'function': 'adb_ui_wifi',
        'isAuto': 'True',
        'txt': 'Disable Wifi whit Wifi OFF',
        'expected result': 'Wifi already disabled, not action was taken.',
        'parameters': {
            'device_id': '1',
            'status': '0',
        }
    },
    {#TC 9
        'function': 'adb_ui_wifi',
        'isAuto': 'True',
        'txt': 'Enable Wifi whit Wifi OFF',
        'expected result': 'Wifi turned ON',
        'parameters': {
            'device_id': '1',
            'status': '1',
        }
    },
    {#TC 10
        'function': 'adb_ui_wifi',
        'isAuto': 'True',
        'txt': 'Enable Wifi whit Wifi ON',
        'expected result': 'Wifi already enabled, not action was taken.',
        'parameters': {
            'device_id': '1',
            'status': '1',
        }
    },
     # === CALCULATOR ===
    {#TC 11
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Add two negative numbers (+)',
        'expected result': 'Correct result',
        'parameters': {
            'device_id': '1',
            'operand1': '-3',
            'operator': '+',
            'operand2': '-2'
        }
    },
    {#TC 12
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Using invalid operator',
        'expected result': 'Invalid operator',
        'parameters': {
            'device_id': '1',
            'operand1': '3',
            'operator': 'x',
            'operand2': '0'
        }
    },
    {#TC 13
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Using letters',
        'expected result': 'Values are not valid',
        'parameters': {
            'device_id': '1',
            'operand1': 'a7b',
            'operator': '+',
            'operand2': '2c'
        }
    },
    {#TC 14
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Add two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '+',
            'operand2': '5'
        }
    },
    {#TC 15
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Subtract 2 numbers (-)',
        'expected result': 'Correct result',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '-',
            'operand2': '5'
        }
    },
    {#TC 16
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Multiply two numbers (*)',
        'expected result': 'Correct result',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '*',
            'operand2': '5'
        }
    },
    {#TC 17
        'function': 'adb_ui_calculator',
        'isAuto': 'True',
        'txt': 'Divide two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '/',
            'operand2': '5'
        }
    },
    # === Calling using ADB ===
    {# TC 18
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 19
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '4492595229',
            'seconds': '3'
        }
    },
    {#TC 20
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '+524492595229',
            'seconds': '3'
        }
    },
    {#TC 21
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 22
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 23
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Number with special characters',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'device_id': '1',
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 24
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Number using letters and numbers',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'device_id': '1',
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 25
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Empty number',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'device_id': '1',
            'number_phone': '',
            'seconds': '3'
        }
    },
    # === CALLING USING UI AUTOMATOR===
    {#TC 26
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 27
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '4494269026',
            'seconds': '3'
        }
    },
    {#TC 28
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '+524494269026',
            'seconds': '3'
        }
    },
    {#TC 29
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 30
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 31
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'Number with special characters',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'device_id': '1',
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 32
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'Number using letters and numbers',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'device_id': '1',
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 33
        'function': 'adb_ui_call',
        'isAuto': 'True',
        'txt': 'Empty number',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'device_id': '1',
            'number_phone': '',
            'seconds': '3'
        }
    },
    # === VOICE MAIL ===
    {#TC 34
        'function': 'ui_voice_message',
        'isAuto': 'True',
        'txt': 'Perform a call using twilio, and leave a voice message',
        'expected result': 'Mensaje de voz encontrado',
        'parameters': {
            'device_id': '1',
            'message':
                'Yo soy un Saiyajin criado en la Tierra.'
                'Por todos los guerreros Saiyajin que asesinaste'
                'Y tambien, por todos los Namekusei que mataste'
                'Juro que te exterminare',
            'to': '+524494269026',
            'from': '+12183327195',
        }
    },
]




