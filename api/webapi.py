from protocol import get_info
from protocol import get_head_position
from protocol import get_temp
from protocol import get_progress
from protocol import get_status

from flask import Flask
from flask import jsonify


app = Flask(__name__)

IP_ADDRESS = 'REPLACE_ME'
PORT = 8899  # default port


@app.route("/")
def index():
    return ''


@app.route("/info")
def info():
    printer_info = get_info({'ip': IP_ADDRESS, 'port': PORT})
    return jsonify(printer_info)


@app.route("/head-location")
def head_location():
    printer_info = get_head_position({'ip': IP_ADDRESS, 'port': PORT})
    return jsonify(printer_info)


@app.route("/temp")
def temp():
    printer_info = get_temp({'ip': IP_ADDRESS, 'port': PORT})
    return jsonify(printer_info)


@app.route("/progress")
def progress():
    printer_info = get_progress({'ip': IP_ADDRESS, 'port': PORT})
    return jsonify(printer_info)


@app.route("/status")
def status():
    printer_info = get_status({'ip': IP_ADDRESS, 'port': PORT})
    return jsonify(printer_info)
