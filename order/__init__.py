from flask import Flask

app = Flask(__name__)

from order import views
