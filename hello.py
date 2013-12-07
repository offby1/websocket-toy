import  collections
from    flask import Flask, request, make_response
from    flask_sockets import Sockets
import  Queue
import  time

messages_by_subscriber = collections.defaultdict(Queue.Queue)

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/echo/')
def echo_socket(ws):
    subscriber_id = ws.receive()
    print("echo_socket: initial message: {!r}".format(subscriber_id))
    while True:
        m = messages_by_subscriber[subscriber_id].get()
        print("echo_socket: m is {}".format(m))
        ws.send(m)

@app.route('/update/<subscriber_id>/', methods=['POST'])
def update(subscriber_id):
    print("update: subscriber_id is {}".format(subscriber_id))
    messages_by_subscriber[subscriber_id].put(request.form['stuff'])
    return make_response(subscriber_id, 204)
