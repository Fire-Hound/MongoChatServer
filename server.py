from gevent.pywsgi import WSGIServer
from chatServer import app, client

http_server = WSGIServer(('0.0.0.0', 40010), app)
http_server.serve_forever()
client.close()