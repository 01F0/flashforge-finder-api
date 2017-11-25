import socket

BUFFER_SIZE = 1024
TIMEOUT_SECONDS = 5


def send_and_receive(printer_adress, message_data):
    """Sends and receives data"""

    printer_socket = socket.socket()
    printer_socket.settimeout(TIMEOUT_SECONDS)
    printer_socket.connect((printer_adress['ip'], printer_adress['port']))
    printer_socket.send(message_data.encode())
    data = printer_socket.recv(BUFFER_SIZE)
    printer_socket.close()

    return data.decode()
