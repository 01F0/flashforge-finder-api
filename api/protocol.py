from packets import request_control_message
from packets import request_info_message
from packets import request_head_position
from packets import request_temp
from packets import request_progress
from packets import request_status

from regex_patterns import regex_for_field
from regex_patterns import regex_for_coordinates
from regex_patterns import regex_for_current_temperature
from regex_patterns import regex_for_target_temperature
from regex_patterns import regex_for_progress
from socket_handler import send_and_receive


import re


def get_info(printer_address):
    """ Returns an object with basic printer information such as name etc."""

    send_and_receive(printer_address, request_control_message)
    info_result = send_and_receive(printer_address, request_info_message)

    printer_info = {}
    info_fields = ['Type', 'Name', 'Firmware', 'SN', 'X', 'Tool Count']
    for field in info_fields:
        regex_string = regex_for_field(field)
        printer_info[field] = re.search(regex_string, info_result).groups()[0]

    return printer_info


def get_head_position(printer_address):
    """ Returns the current x/y/z coordinates of the printer head. """

    send_and_receive(printer_address, request_control_message)
    info_result = send_and_receive(printer_address, request_head_position)

    printer_info = {}
    printer_info_fields = ['X', 'Y', 'Z']
    for field in printer_info_fields:
        regex_string = regex_for_coordinates(field)
        printer_info[field] = re.search(regex_string, info_result).groups()[0]

    return printer_info


def get_temp(printer_address):
    """ Returns printer temp. Both targeted and current. """

    send_and_receive(printer_address, request_control_message)
    info_result = send_and_receive(printer_address, request_temp)

    regex_temp = regex_for_current_temperature()
    regex_target_temp = regex_for_target_temperature()
    temp = re.search(regex_temp, info_result).groups()[0]
    target_temp = re.search(regex_target_temp, info_result).groups()[0]

    return {'Temperature': temp, 'TargetTemperature': target_temp}


def get_progress(printer_address):
    send_and_receive(printer_address, request_control_message)
    info_result = send_and_receive(printer_address, request_progress)

    regex_groups = re.search(regex_for_progress(), info_result).groups()
    printed = regex_groups[0]
    total = regex_groups[1]
    percentage = int((int(printed) / int(total)) * 100)

    return {'BytesPrinted': printed, 'BytesTotal': total, 'PercentageCompleted': percentage}


def get_status(printer_address):
    """ Returns the current printer status. """

    send_and_receive(printer_address, request_control_message)
    info_result = send_and_receive(printer_address, request_status)

    printer_info = {}
    printer_info_fields = ['Status', 'MachineStatus', 'MoveMode', 'Endstop']
    for field in printer_info_fields:
        regex_string = regex_for_field(field)
        printer_info[field] = re.search(regex_string, info_result).groups()[0]

    return printer_info
