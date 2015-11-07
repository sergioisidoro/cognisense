from gevent.monkey import patch_all
patch_all()

from cortex.api.api import app

app.run(debug=True)
