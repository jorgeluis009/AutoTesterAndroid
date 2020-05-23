#My JSON
myJson2 = [
    # === VOICE MAIL ===
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
        'txt': 'Enable Wifi',
        'expected result': 'Wi-fi turned On',
        'parameters': {
            'option': '1'
        }
    },
    {  # TC 6
        'function': 'calculatorUI',
        'txt': 'Add two negative numbers (+)',
        'expected result': 'Correct result',
        'parameters': {
            'num_1': '-3',
            'operator': '+',
            'num_2': '-2'
        }
    },
    {  # TC 13
        'function': 'callUI',
        'txt': 'Call Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'number_phone': '9159951',
            'seconds': '3'
        }
    },
    {  # TC 21
        'function': 'voicemailUI',
        'txt': 'Perform a call using twilio, and leave a voice message',
        'expected result': 'Mensaje de voz encontrado',
        'parameters': {
            'message':
                'Por todos los guerreros Sayayin que asesinaste'
                'Y tambien, por todos los Namekusei que mataste'
                'Juro que te exterminare',
            'to': '+524492595229',
            'from': '+13612035605',
        }
    },
]