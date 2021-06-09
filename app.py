from flask import Flask
from RPI import rpi_connect

app = Flask(__name__)


@app.route('/heartbeat', methods=['GET'])
def heart_beat():
    return 'Raspberry-pi is Active'


@app.route('/gpio_on', methods=['GET'])
def turn_on_led():
    # rpi_connect
    return

if __name__ == '__main__':
    app.run()
