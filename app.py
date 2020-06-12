from flask import Flask
from src.blueprints.api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def index():
	return "hello world"

if __name__ == "__main__":
	app.run(port=8080, debug=True, threaded=True)
