from flask import Flask
from api.blueprints.api import api
from api.blueprints.error import error
import requests

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(error)

if __name__ == "__main__":
	try:
		print("Starting api..")
		app.run(port=8080, debug=True, threaded=True)
	except KeyboardInterrupt:
		print("Api stopped!")
		pass