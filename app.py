from flask import Flask, request, render_template, url_for
from src.blueprints.api import api
from src.blueprints.error import error
import requests

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
	headers = {"Content-Type": "application/json"}
	#r = requests.post("http://localhost:8080/api/inventory", json=body, headers=headers).content
	r = requests.post("http://localhost:8080/api/inventory", json=body, headers=headers)
	data =  r.json()
	items = []
	for i in data["inv"]:
		items.append(i)
	print(items)
	return "items"

@app.route("/test")
def test():
	#return requests.get("http://localhost:8080/api/inventory/refresh/76561198439884801").json
	return requests.post("http://localhost:8080/api/user", json={"steamkey": "123"}, headers={"Content-Type": "application/json"}).content # send get request with json body

if __name__ == "__main__":
	app.run(port=8080, debug=True, threaded=True)