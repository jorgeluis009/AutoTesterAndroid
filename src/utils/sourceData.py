#My JSON
myJson = [
    # ===  identify Devices functions ===
    {#TC 1
        'function': 'detectDevices',
        'txt': 'Device detected',
        'expected result': 'Device connected',
        'parameters': {}
    },
    # === WIFI TC ===
    {#TC 2
        'function': 'wifiUI',
        'txt': 'Disable Wifi whit Wifi ON',
        'expected result': 'Wi-fi turned Off',
        'parameters': {
            'option': '0'
        }
    },
    {#TC 3
        'function': 'wifiUI',
        'txt': 'Disable Wifi whit Wifi OFF',
        'expected result': 'Wifi is Off already, not action was taken',
        'parameters': {
            'option': '0'
        }
    },
    {#TC 4
        'function': 'wifiUI',
        'txt': 'Enable Wifi whit Wifi OFF',
        'expected result': 'Wifi turned ON',
        'parameters': {
            'option': '1'
        }
    },
    {#TC 5
        'function': 'wifiUI',
        'txt': 'Enable Wifi whit Wifi ON',
        'expected result': 'Wifi is On already, not action was taken.',
        'parameters': {
            'option': '1'
        }
    },
     # === CALCULATOR ===
    {#TC 6
        'function': 'calculatorUI',
        'txt': 'Add two negative numbers (+)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '-3',
            'operator': '+',
            'num_2': '-2'
        }
    },
    {#TC 7
        'function': 'calculatorUI',
        'txt': 'Using invalid operator',
        'expected result': 'Invalid operator',
        'parameters': {
            'num_1': '3',
            'operator': 'x',
            'num_2': '0'
        }
    },
    {#TC 8
        'function': 'calculatorUI',
        'txt': 'Using letters',
        'expected result': 'Values are not valid',
        'parameters': {
            'num_1': 'a7b',
            'operator': '+',
            'num_2': '2c'
        }
    },
    {#TC 9
        'function': 'calculatorUI',
        'txt': 'Add two numbers',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '+',
            'num_2': '5'
        }
    },
    {#TC 10
        'function': 'calculatorUI',
        'txt': 'Subtract 2 numbers (-)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '-',
            'num_2': '5'
        }
    },
    {#TC 11
        'function': 'calculatorUI',
        'txt': 'Multiply two numbers (*)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '4',
            'operator': '*',
            'num_2': '5'
        }
    },
    {#TC 12
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
    {#TC 13
        'function': 'callUI',
        'txt': 'Call Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 14
        'function': 'callUI',
        'txt': 'Call National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4492595229',
            'seconds': '3'
        }
    },
    {#TC 15
        'function': 'callUI',
        'txt': 'Call International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'number_phone': '+524494269026',
            'seconds': '3'
        }
    },
    {#TC 16
        'function': 'callUI',
        'txt': 'Call Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 17
        'function': 'callUI',
        'txt': 'Call Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 18
        'function': 'callUI',
        'txt': 'Call Number with special characters',
        'expected result': 'Invalid number',
        'parameters': {
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 19
        'function': 'callUI',
        'txt': 'Call Number using letters and numbers',
        'expected result': 'Invalid number',
        'parameters': {
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 20
        'function': 'callUI',
        'txt': 'Call Empty number',
        'expected result': 'Invalid number',
        'parameters': {
            'number_phone': '',
            'seconds': '3'
        }
    },
    # === VOICE MAIL ===
    {#TC 21
        'function': 'voicemailUI',
        'txt': 'Perform a call using twilio, and leave a voice message',
        'expected result': 'Voicemail found',
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
    {# TC 22
        'function': 'callADB',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {#TC 23
        'function': 'callADB',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4492595229',
            'seconds': '3'
        }
    },
    {#TC 24
        'function': 'callADB',
        'txt': 'International number (using + prefix)',
        'expected result': 'Call to +5214492595229 was successful',
        'parameters': {
            'number_phone': '+524492595229',
            'seconds': '3'
        }
    },
    {#TC 25
        'function': 'callADB',
        'txt': 'Emergency number using *',
        'expected result': 'Call to *811 was successful',
        'parameters': {
            'number_phone': '*811',
            'seconds': '3'
        }
    },
    {#TC 26
        'function': 'callADB',
        'txt': 'Number using #',
        'expected result': 'Call to #311 was successful',
        'parameters': {
            'number_phone': '#311',
            'seconds': '3'
        }
    },
    {#TC 27
        'function': 'callADB',
        'txt': 'Number with special characters',
        'expected result': 'Invalid number',
        'parameters': {
            'number_phone': '!449^%',
            'seconds': '3'
        }
    },
    {#TC 28
        'function': 'callADB',
        'txt': 'Number using letters and numbers',
        'expected result': 'Invalid number',
        'parameters': {
            'number_phone': '123test456',
            'seconds': '3'
        }
    },
    {#TC 29
        'function': 'callADB',
        'txt': 'Empty number',
        'expected result': 'Invalid number',
        'parameters': {
            'number_phone': '',
            'seconds': '3'
        }
    }
]




