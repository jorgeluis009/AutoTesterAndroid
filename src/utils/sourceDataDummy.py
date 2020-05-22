#My JSON
myJson2 = [
    # ===  identify Devices functions ===
    # {  # TC 2
    #     'function': 'detectDevices',
    #     'txt': 'Un dispositivo conectado',
    #     'expected result': 'Serial 1 = R28M410479V-',
    #     'parameters': {}
    # },
    {  # TC 34
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
    # {#TC 26
    #     'function': 'callUI',
    #     'isAuto': 'True',
    #     'txt': 'Local number',
    #     'expected result': 'Call to 9159951 was successful',
    #     'parameters': {
    #         'device_id': '1',
    #         'number_phone': '9159951',
    #         'seconds': '3'
    #     }
    # },
    # {  # TC 18
    #     'function': 'adb_call',
    #     'txt': 'Local number',
    #     'expected result': 'Call to 9159951 was successful',
    #     'parameters': {
    #         'device_id': '1',
    #         'number_phone': '9159951'
    #     }
    # },
    # === VOICE MAIL ===
    # {#TC 34
    #     'function': 'ui_voice_message',
    #     'txt': 'Perform a call using twilio, and leave a voice message',
    #     'expected result': 'Mensaje de voz encontrado',
    #     'parameters': {
    #         'device_id': '1',
    #         'message':
    #             'Yo soy un Saiyajin criado en la Tierra. '
    #             'Por todos los guerreros Saiyajin que asesinaste'
    #             'Y tambien, por todos los Namekusei que mataste'
    #             'Juro que te exterminare',
    #         'to': '+524492595229',
    #         'from': '+17547048255',
    #     }
    # },
    # {  # TC 26
    #     'function': 'adb_ui_call',
    #     'isAuto': 'True',
    #     'txt': 'Local number',
    #     'expected result': 'Call to 9159951 was successful',
    #     'parameters': {
    #         'device_id': '1',
    #         'number_phone': '9159951',
    #         'seconds': '3'
    #     }
    # },
]




