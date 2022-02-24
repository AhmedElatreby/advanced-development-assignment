from flask import Flask

app = Flask(__name__)

from items import views
