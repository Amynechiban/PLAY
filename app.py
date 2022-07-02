from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session


app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start')
def login():
    return render_template('start.html')


@app.route('/chat')
def chat():
   return render_template('Chat.html')


def messageRecived():
  print( 'message was received!!!' )



@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )


if __name__ == '__main__':
  socketio.run( app, debug = False, host='0.0.0.0' )