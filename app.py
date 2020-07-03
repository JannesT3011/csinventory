from flask import Flask
from src.blueprints.api import api
from src.blueprints.error import error
import requests

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(error)

if __name__ == "__main__":
	app.run(port=8080, debug=True, threaded=True)