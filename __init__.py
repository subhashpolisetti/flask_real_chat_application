# __init__.py
from flask import Flask
from config import Config
from flask_socketio import SocketIO
from models import db

# Initialize socketio and db here
socketio = SocketIO()
db = db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    socketio.init_app(app)

    # Register the chat route without importing from app.py
    from controllers import chat_controller
    app.add_url_rule('/', view_func=chat_controller.chat_home)

    return app

