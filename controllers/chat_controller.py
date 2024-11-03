# controllers/chat_controller.py
from flask import render_template, request
from flask_socketio import join_room, leave_room, emit
from models import ChatMessage, db
from datetime import datetime
from __init__ import socketio  # Import socketio from __init__.py to avoid circular import

def chat_home():
    return render_template('chat_room.html')

@socketio.on('join_chat')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    
    previous_messages = ChatMessage.query.filter_by(chat_room=room).order_by(ChatMessage.timestamp).all()
    for message in previous_messages:
        emit('message', {
            'sender': message.sender,
            'content': message.content,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }, room=request.sid)
    
    emit('message', {'content': f"{username} has joined the chat."}, room=room)

@socketio.on('send_message')
def handle_message(data):
    room = data['room']
    username = data['username']
    message_content = data['content']
    
    new_message = ChatMessage(chat_room=room, sender=username, content=message_content)
    db.session.add(new_message)
    db.session.commit()
    
    emit('message', {
        'sender': username,
        'content': message_content,
        'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }, room=room)

@socketio.on('leave_chat')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('message', {'content': f"{username} has left the chat."}, room=room)
