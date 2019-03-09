import socketio
import requests

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on('my message')
def on_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.on('welcome')
def on_welcome(data):
    print('welcome: ', data)

@sio.on('time')
def on_welcome(data):
    print('time: ', data)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5555')
sio.wait()
