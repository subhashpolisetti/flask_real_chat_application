from __init__ import create_app, socketio
from models import db

app = create_app()

# Initialize the database (run only once to create tables)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5002)

