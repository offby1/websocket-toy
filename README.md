Websocket example.

- Start the server via ``gunicorn -k flask_sockets.worker hello:app``

- Point yon browser at file:///.../ws.html

- Invoke ye shell command ``curl -d 'stuff=what it is' http://127.0.0.1:8000/update/1234/``

You should see the message appear immediately in the browser.

Further cute tricks:

Preload a bunch of messages:

- ``curl -d 'stuff=One singular sensation' http://127.0.0.1:8000/update/1/``
- ``curl -d 'stuff=Two, two, two mints in one' http://127.0.0.1:8000/update/2/``
- ``curl -d 'stuff=Three branches of government' http://127.0.0.1:8000/update/3/``

Now edit the html file, changing the ``1234`` to ``1``, and reload;
you should see the message for one.  Change it again to ``2``, reload,
you'll see the message for 2, etc.
