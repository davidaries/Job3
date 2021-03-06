"""This class contains the language dictionary to be used in other classes of this program
:param english: this dictionary contains the english vocabulary used in this program.  Based on the key value
    the corresponding word is returned.  The layout for the key value is '~NUMBER'
:type english: dict
:param spanish: this dictionary contains the spanish vocabulary used in this program.  Based on the key value
    the corresponding word is returned.  The layout for the key value is '~NUMBER'
:type spanish: dict
:param language_dictionary: this dictionary contains both english and spanish dictionaries for easy access
    to both dictionaries.  It allows language preference (~101 for english) (~102 for spanish) to be used
    as a key to link to the corresponding dictionary and retrieve the specific word requested
:type language_dictionary: dict
"""
english = {
    '~1': 'Name',
    '~2': 'diagnosis',
    '~3': 'treat',
    '~4': 'Hello! Please treat:',
    '~5': 'flu',
    '~6': 'Pause',
    '~7': 'Un Pause',
    '~8': 'End',
    '~9': 'Event',
    '~10': 'Time',
    '~11': 'Job',
    '~12': 'Timer',
    '~13': 'Log',
    '~14': 'Sex',
    '~15': 'Age',
    '~16': 'Phone',
    '~17': 'Chief Complaint',
    '~18': 'Test',
    '~19': 'Weight',
    '~20': 'Submit',
    '~21': 'Male',
    '~22': 'Female',

    '~23': 'Role',
    '~24': 'Receptionist',
    '~25': 'Assistant',
    '~26': 'Provider',
    '~27': 'Lab Technician',
    '~28': 'Headache',
    '~29': 'Fever',
    '~30': 'COVID',
    '~31': 'Flu Test',
    '~32': 'Coronavirus Test',
    '~33': 'Task',
    '~34': 'Receive',
    '~35': 'Room',
    '~36': 'Diagnose',
    '~101': 'English',
    '~102': 'Spanish'
}

spanish = {
    '~1': 'Nombre',
    '~2': 'diagnostico',
    '~3': 'curar',
    '~4': 'Hola! Por favor curar:',
    '~5': 'gripe',
    '~6': 'Pausa',
    '~7': 'Reanudar',
    '~8': 'Fin',
    '~9': 'Evento',
    '~10': 'Hora',
    '~11': 'Trabajo',
    '~12': 'Temporizador',
    '~13': 'Sesion',
    '~14': 'Sexo',
    '~15': 'Edad',
    '~16': 'Teléfono',
    '~17': 'Problema',
    '~18': 'Prueba',
    '~19': 'Peso',
    '~20': 'Enviar',
    '~21': 'Hombre',
    '~22': 'Mujer',
    '~23': 'Cargo',
    '~24': 'Recepcionista',
    '~25': 'Asistente',
    '~26': 'Doctor',
    '~27': 'Técnico de Laboratorio',
    '~28': 'dolor de cabeza',
    '~29': 'fiebre',
    '~30': 'COVID',
    '~31': 'Flu Test',
    '~32': 'Coronavirus Test',
    '~33': 'Tarea',
    '~34': 'Receive',
    '~35': 'Dar una habitacion',
    '~36': 'Diagnosticar',
    '~101': 'ingles',
    '~102': 'espanol'
}

language_dictionary = {
    "~101": english,
    "~102": spanish
}


def get_text_from_dict(language, text):
    """Function for returning the requested value from the dictionary
    Args:
    :param language: string in format ('~101' for english) ('~102' for spanish) used as a key to choose which
        language dictionary should be returned
    :type language: str
    :param text: string in form '~NUMBER' used to get the specific word from the dictionaries listed above
    :type text: str
    :return: is the requested dictionary value based language and text keys given to the function
    :rtype: str"""
    return language_dictionary.get(language).get(text)
