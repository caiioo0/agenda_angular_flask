from flask import Flask
from app.modules.xpto.xpto_routes import xpto_routes

app = Flask(__name__)

app.register_blueprint(xpto_routes)

