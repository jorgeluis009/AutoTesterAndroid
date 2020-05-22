#My JSON
myJson = [
    # ===  identify Devices functions ===
    {#TC 1
        'function': 'detectDevices',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
        'parameters': {}
    },
    # === WIFI TC ===
    {#TC 7
        'function': 'wifiUI',
        'txt': 'Disable Wifi whit Wifi ON',
        'expected result': 'Wi-fi turned Off',
        'parameters': {
            'option': '0'
        }
    },
    {#TC 8
        'function': 'wifiUI',
        'txt': 'Disable Wifi whit Wifi OFF',
        'expected result': 'Wifi is Off already, not action was taken',
        'parameters': {
            'option': '0'
        }
    },
    {#TC 9
        'function': 'wifiUI',
        'txt': 'Enable Wifi whit Wifi OFF',
        'expected result': 'Wifi turned ON',
        'parameters': {
            'option': '1'
        }
    },
    {#TC 10
        'function': 'wifiUI',
        'txt': 'Enable Wifi whit Wifi ON',
        'expected result': 'Wifi is On already, not action was taken.',
        'parameters': {
            'option': '1'
        }
    },
     # === CALCULATOR ===
    {#TC 11
        'function': 'calculatorUI',
        'txt': 'Add two negative numbers (+)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '-3',
            'operator': '+',
            'num_2': '-2'
        }
    },
    {#TC 12
        'function': 'calculatorUI',
        'txt': 'Using invalid operator',
        'expected result': 'Invalid operator',
        'parameters': {
            'num_1': '3',
            'operator': 'x',
            'num_2': '0'
        }
    },
    {#TC 13
        'function': 'calculatorUI',
        'txt': 'Using letters',
        'expected result': 'Values are not valid',
        'parameters': {
            'num_1': 'a7b',
            'operator': '+',
            'num_2': '2c'
        }
    },
    {#TC 14
        'function': 'calculatorUI',
        'txt': 'Add two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '+',
            'num_2': '5'
        }
    },
    {#TC 15
        'function': 'calculatorUI',
        'txt': 'Subtract 2 numbers (-)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '-',
            'num_2': '5'
        }
    },
    {#TC 16
        'function': 'calculatorUI',
        'txt': 'Multiply two numbers (*)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '*',
            'num_2': '5'
        }
    },
    {#TC 17
        'function': 'calculatorUI',
        'txt': 'Divide two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '/',
            'num_2': '5'
        }
    },
    # === CALLING USING UI AUTOMATOR===
    {#TC 26
        'function': 'callUI',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 27
        'function': 'callUI',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4492595229',
            'seconds': '3'
        }
    },
    {#TC 28
        'function': 'callUI',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'number_phone': '+524494269026',
            'seconds': '3'
        }
    },
    {#TC 29
        'function': 'callUI',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 30
        'function': 'callUI',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 31
        'function': 'callUI',
        'txt': 'Number with special characters',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 32
        'function': 'callUI',
        'txt': 'Number using letters and numbers',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 33
        'function': 'callUI',
        'txt': 'Empty number',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '',
            'seconds': '3'
        }
    },
    # === VOICE MAIL ===
    {#TC 34
        'function': 'voicemailUI',
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
     # === Calling using ADB ===
    {# TC 18
        'function': 'callADB',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 19
        'function': 'callADB',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4492595229',
            'seconds': '3'
        }
    },
    {#TC 20
        'function': 'callADB',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'number_phone': '+524492595229',
            'seconds': '3'
        }
    },
    {#TC 21
        'function': 'callADB',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 22
        'function': 'callADB',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 23
        'function': 'callADB',
        'txt': 'Number with special characters',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 24
        'function': 'callADB',
        'txt': 'Number using letters and numbers',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 25
        'function': 'callADB',
        'txt': 'Empty number',
        'expected result': 'Numero de telefono invalido',
        'parameters': {
            'number_phone': '',
            'seconds': '3'
        }
    }
]




