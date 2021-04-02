from protocol import get_info
from protocol import get_head_position
from protocol import get_temp
from protocol import get_progress
from protocol import get_status

from flask import Flask
from flask import jsonify

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

PORT = 8899  # default port


@app.route("/")
def index():
    return ''


@app.route("/<string:ip_address>/info")
def info(ip_address):
    printer_info = get_info({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/head-location")
def head_location(ip_address):
    printer_info = get_head_position({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/temp")
def temp(ip_address):
    printer_info = get_temp({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/progress")
def progress(ip_address):
    printer_info = get_progress({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/status")
def status(ip_address):
    printer_info = get_status({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)
