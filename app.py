from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_cors import CORS

import logging
logging.basicConfig(level=logging.INFO)

from iotsitewise import update_sitewise

app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins="*")
led_status_global = False

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/change_led_web_hook', methods=['POST'])
def change_led_web_hook():
    
    led_status = bool(request.get_json()["led_on"])
    
    try:  
        update_sitewise(led_status) 
    except Exception as e:
        app.logger.info(str(e))
        return str(e),400
    
    global led_status_global
    led_status_global = led_status
    
    socketio.emit('led_status', led_status)
    return '', 200

@socketio.on('connect')
def handle_connect():
    socketio.emit('led_status', False)  

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)