from flask import Flask, request, render_template
from src.blueprints.api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def index():
	return "hello world"

@app.route("/inventory", methods=["GET", "POST"])
def inventory():
	steamid = request.form.get("search-id")
	body = {
		"steamid": steamid,
		"api_key": ""
	}
	return "Handle search id form and return inv from db"

if __name__ == "__main__":
	app.run(port=8080, debug=True, threaded=True)
