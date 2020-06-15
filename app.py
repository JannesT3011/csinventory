from flask import Flask, request, render_template
from src.blueprints.api import api
from src.blueprints.error import error

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(error)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/inventory", methods=["POST"])
def inventory():
	steamid = request.form["search-id"]
	body = {
		"steamid": steamid,
		"api_key": ""
	}
	return body

if __name__ == "__main__":
	app.run(port=8080, debug=True, threaded=True)
