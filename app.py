import os

import redis
from flask import Flask
from flask_cors import CORS
from flask_session import Session

from db.views import db
from items.views import items
from login.views import login
from navigation.views import navigation
from order.views import order

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(12).hex()
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = redis.from_url(
    "redis://:AgjCjPpFIXTwNfVvDffTRyPCIZrmrGmr@redis-12062.c1.us-central1-2.gce.cloud.redislabs.com:12062"
)
app.register_blueprint(navigation)
app.register_blueprint(items)
app.register_blueprint(order)
app.register_blueprint(login)
app.register_blueprint(db)

Session(app)
CORS(app)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
