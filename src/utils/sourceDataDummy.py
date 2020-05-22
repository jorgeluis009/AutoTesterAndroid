#My JSON
myJson2 = [
    # ===  identify Devices functions ===
    {#TC 1
        'function': 'detectDevices',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
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
    # === CALLING USING UI AUTOMATOR===
    {#TC 14
        'function': 'callUI',
        'txt': 'National number',
        'expected result': 'Call to 4492595229 was successful',
        'parameters': {
            'number_phone': '4492595229',
            'seconds': '3'
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


    # {#TC 28
    #     'function': 'callADB',
    #     'txt': 'Number using letters and numbers',
    #     'expected result': 'Numero de telefono invalido',
    #     'parameters': {
    #         'number_phone': '123test456',
    #         'seconds': '3'
    #     }
    # },
    # {#TC 29
    #     'function': 'callADB',
    #     'txt': 'Empty number',
    #     'expected result': 'Numero de telefono invalido',
    #     'parameters': {
    #         'number_phone': '',
    #         'seconds': '3'
    #     }
    # }
    # === VOICE MAIL ===
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
            'from': '+17547048255',
        }
    }
]