from flask import Flask
from RPI import rpi_connect
from flask_cors import CORS, cross_origin
import threading

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/heartbeat', methods=['GET'])
def heart_beat():
    return 'Raspberry-pi is Active'


@app.route('/gpio_on', methods=['GET'])
def turn_on_led():
    thread = threading.Thread(target=pi_thread)
    thread.start()
    return "OK"


def pi_thread():
    rpi_connect.on_notifier()


if __name__ == '__main__':
    app.run()
