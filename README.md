# Flask Real-Time Chat Application

This is a real-time chat application built with Flask, Flask-SocketIO, and SQLite. Users can join chat rooms, send messages, and view message history in real-time. The app features a simple and responsive UI that provides a smooth chat experience.

## Features

- Real-time messaging with WebSocket support using Flask-SocketIO
- Chat rooms with unique room names
- Message history saved in SQLite database
- Responsive and clean UI
- Python `.env` file support for secure configurations

## Project Structure

```
flask_chat_mvc/
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── models.py               # Database models
├── controllers/
│   └── chat_controller.py  # Controller for handling routes and socket events
├── templates/
│   └── chat_room.html      # HTML template for chat room
├── static/
│   └── styles.css          # CSS file for styling
└── __init__.py             # Flask app setup
```

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (recommended)
- Git

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/flask_real_chat_application.git
   cd flask_chat_mvc
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Mac/Linux
   # venv\Scripts\activate    # For Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


4. **Initialize the Database:**

   Run the following command to initialize the SQLite database:

   ```bash
   python app.py
   ```

   The application will create a file named `chat_history.db` in the project directory.

### Running the Application

1. **Start the Flask Application:**

   ```bash
   python app.py
   ```

2. **Access the Application:**

   Open a web browser and go to:

   ```
   Ex:  http://127.0.0.1:5003
   ```

3. **Join a Chat Room:**

   - Enter your username and a room name to join the chat.
   - You can open multiple tabs with the same room name to test real-time messaging.

### Using the Application

- **Join Chat Room:** Enter a username and room name, then click "Join Chat."
- **Send Messages:** Type messages in the input box and click "Send" to communicate in real-time.
- **Message History:** View previously sent messages within the room.

### Application Screenshots

![Chat Application UI](static/images/img-1.png)

![Chat Application UI](static/images/img-2.png)

## File Descriptions

- **app.py:** The main entry point of the application, where the server is run.
- **config.py:** Contains configuration settings for the Flask application.
- **models.py:** Defines the `ChatMessage` model for storing messages in the SQLite database.
- **controllers/chat_controller.py:** Contains the main route and WebSocket event handlers.
- **templates/chat_room.html:** The HTML file for the chat room interface.
- **static/styles.css:** CSS file to style the chat application.

## Technologies Used

- **Flask** - Micro web framework for Python
- **Flask-SocketIO** - Provides WebSocket support for real-time communication
- **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask for ORM
- **SQLite** - Lightweight database for message storage
- **HTML/CSS** - Frontend design and styling

