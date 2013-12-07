Websocket example.

- Start the server via ``gunicorn -k flask_sockets.worker hello:app``

- Point yon browser at file:///.../ws.html

- Invoke ye shell command ``curl -d 'stuff=what it is' http://127.0.0.1:8000/update/``

You should see the message appear immediately in the browser.
