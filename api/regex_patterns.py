def regex_for_field(field_name):
    """Machine Type: Flashforge Finder"""

    return field_name + ': ?(.+?)\\r\\n'


def regex_for_coordinates(field_name):
    """ X:-19.19 Y:6 Z:7.3 A:846.11 B:0 """
    return field_name + ':(.+?) '


def regex_for_current_temperature():
    """T0:210 /210 B:0 /0"""

    return 'T0:([0-9].*?) '


def regex_for_target_temperature():
    """ T0:210 /210 B:0 /0 """

    return '\/([0-9].*?) '


def regex_for_progress():
    """ T0:210 /210 B:0 /0 """

    return '([0-9].*)\/([0-9].*?)\\r'
