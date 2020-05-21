#My JSON
myJson2 = [
    # ===  identify Devices functions ===
    {#TC 1
        'function': 'read_devices',
        'isAuto': 'False',
        'txt': 'Ningun dispositivo conectado',
        'expected result': 'No se encontro ningun dispositivo',
        'parameters': {}
    },
    {  # TC 2
        'function': 'read_devices',
        'isAuto': 'False',
        'txt': 'Un dispositivo conectado',
        'expected result': 'Serial 1 = R28M410479V-',
        'parameters': {}
    },
    {  # TC 18
        'function': 'adb_call',
        'isAuto': 'False',
        'txt': 'Local number',
        'expected result': 'Call to 9159951 was successful',
        'parameters': {
            'device_id': '1',
            'number_phone': '9159951'
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
                'Yo soy un Saiyajin criado en la Tierra. '
                'Por todos los guerreros Saiyajin que asesinaste'
                'Y tambien, por todos los Namekusei que mataste'
                'Juro que te exterminare',
            'to': '+524494269026',
            'from': '+17547048255',
        }
    },
]




