from gevent.monkey import patch_all
patch_all()

from cortex.api.api import app

from gevent.wsgi import WSGIServer

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
