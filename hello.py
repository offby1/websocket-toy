from flask import Flask, request, make_response
from flask_sockets import Sockets
import Queue
import time

messages = Queue.Queue()

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        ws.send(messages.get())

@app.route('/update/', methods=['POST'])
def update():
    print("Ayup")
    messages.put(request.form['stuff'])
    return make_response('groovy', 204)
