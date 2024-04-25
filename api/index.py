from gevent import monkey
monkey.patch_all()

from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)

# Используйте gevent в качестве асинхронного режима для SocketIO
socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")
CORS(app)  # Включение CORS для всех источников

@app.route('/flows/trigger/d3a740f4-8aef-4688-a591-d8bed4373cb7', methods=['POST'])
def update_room():
    data = request.json
    # Отправка события всем подключённым клиентам
    socketio.emit('update', data)
    return {"success": True}, 200

if __name__ == '__main__':
    # Запуск Flask-приложения с использованием gevent
    socketio.run(app, debug=False, host='0.0.0.0', port=8081)
