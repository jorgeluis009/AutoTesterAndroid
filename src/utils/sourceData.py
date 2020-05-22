#My JSON
myJson = [
    # ===  identify Devices functions ===
    {#TC 1
        'function': 'read_devices',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
        'parameters': {}
    },
    {#TC 2
        'function': 'read_devices',
        'txt': 'Un dispositivo conectado',
        'expected result': 'Serial 1 = R28M30VCACV-',
        'parameters': {}
    },
    {#TC 3
        'function': 'read_devices',
        'txt': 'Dos o mas dispositivos conectados',
        'expected result': '?',
        'parameters': {}
    },
    {#TC 4
        'function': 'read_device',
        'txt': 'Un dispositivo conectado',
        'expected result': 'Serial = R28M410479V',
        'parameters': {}
    },
    {#TC 5
        'function': 'read_device',
        'txt': 'Un dispositivo conectado',
        'expected result': 'list index out of range',
        'parameters': {}
    },
    {#TC 6
        'function': 'read_device',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
        'parameters': {}
    },
    # === WIFI TC ===
    {#TC 7
        'function': 'adb_ui_wifi',
        'txt': 'Disable Wifi whit Wifi ON',
        'expected result': 'Wi-fi turned Off',
        'parameters': {
            'option': '0'
        }
    },
    {#TC 8
        'function': 'adb_ui_wifi',
        'txt': 'Disable Wifi whit Wifi OFF',
        'expected result': 'Wifi is Off already, not action was taken',
        'parameters': {
            'option': '0'
        }
    },
    {#TC 9
        'function': 'adb_ui_wifi',
        'txt': 'Enable Wifi whit Wifi OFF',
        'expected result': 'Wifi turned ON',
        'parameters': {
            'option': '1'
        }
    },
    {#TC 10
        'function': 'adb_ui_wifi',
        'txt': 'Enable Wifi whit Wifi ON',
        'expected result': 'Wifi is On already, not action was taken.',
        'parameters': {
            'option': '1'
        }
    },
     # === CALCULATOR ===
    {#TC 11
        'function': 'adb_ui_calculator',
        'txt': 'Add two negative numbers (+)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '-3',
            'operator': '+',
            'num_2': '-2'
        }
    },
    {#TC 12
        'function': 'adb_ui_calculator',
        'txt': 'Using invalid operator',
        'expected result': 'Invalid operator',
        'parameters': {
            'num_1': '3',
            'operator': 'x',
            'num_2': '0'
        }
    },
    {#TC 13
        'function': 'adb_ui_calculator',
        'txt': 'Using letters',
        'expected result': 'Values are not valid',
        'parameters': {
            'num_1': 'a7b',
            'operator': '+',
            'num_2': '2c'
        }
    },
    {#TC 14
        'function': 'adb_ui_calculator',
        'txt': 'Add two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '+',
            'num_2': '5'
        }
    },
    {#TC 15
        'function': 'adb_ui_calculator',
        'txt': 'Subtract 2 numbers (-)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '-',
            'num_2': '5'
        }
    },
    {#TC 16
        'function': 'adb_ui_calculator',
        'txt': 'Multiply two numbers (*)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '*',
            'num_2': '5'
        }
    },
    {#TC 17
        'function': 'adb_ui_calculator',
        'txt': 'Divide two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '/',
            'num_2': '5'
        }
    },
    # === Calling using ADB ===
    {# TC 18
        'function': 'adb_call',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 19
        'function': 'adb_call',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4492595229',
            'seconds': '3'
        }
    },
    {#TC 20
        'function': 'adb_call',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'number_phone': '+524492595229',
            'seconds': '3'
        }
    },
    {#TC 21
        'function': 'adb_call',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 22
        'function': 'adb_call',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 23
        'function': 'adb_call',
        'txt': 'Number with special characters',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 24
        'function': 'adb_call',
        'txt': 'Number using letters and numbers',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 25
        'function': 'adb_call',
        'txt': 'Empty number',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '',
            'seconds': '3'
        }
    },
    # === CALLING USING UI AUTOMATOR===
    {#TC 26
        'function': 'adb_ui_call',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 27
        'function': 'adb_ui_call',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4494269026',
            'seconds': '3'
        }
    },
    {#TC 28
        'function': 'adb_ui_call',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'number_phone': '+524494269026',
            'seconds': '3'
        }
    },
    {#TC 29
        'function': 'adb_ui_call',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 30
        'function': 'adb_ui_call',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 31
        'function': 'adb_ui_call',
        'txt': 'Number with special characters',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 32
        'function': 'adb_ui_call',
        'txt': 'Number using letters and numbers',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 33
        'function': 'adb_ui_call',
        'txt': 'Empty number',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '',
            'seconds': '3'
        }
    },
    # === VOICE MAIL ===
    {#TC 34
        'function': 'ui_voice_message',
        'txt': 'Perform a call using twilio, and leave a voice message',
        'expected result': 'Mensaje de voz encontrado',
        'parameters': {
            'message':
                'Por todos los guerreros Sayayin que asesinaste'
                'Y tambien, por todos los Namekusei que mataste'
                'Juro que te exterminare',
            'to': '+524492595229',
            'from': '+17547048255',
        }
    },
]




