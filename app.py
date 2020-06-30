from flask import Flask, request, render_template, url_for, jsonify
from src.blueprints.api import api
from src.blueprints.error import error
import requests

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(error)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/inventory", methods=["GET","POST"])
def inventory():
	try:
		steamid = request.form["search-id"]
		update = False
	except:
		steamid = request.get_json()["steamid"]
		update = request.get_json()["update"]
	body = {
		"steamid": steamid,
		"api_key": "",
		"update": update
	}
	headers = {"Content-Type": "application/json"}
	#r = requests.post("http://localhost:8080/api/inventory", json=body, headers=headers).content
	r = requests.post("http://localhost:8080/api/inventory", json=body, headers=headers)
	data =  r.json()
	#print(data["_id"])
	items = []
	for item in data:
		if item == "inventory_amount" or item == "inventory_value_median" or item == "todays_cashout":
			pass
		else:
			items.append({"name": item, "data": data[item]})
	#print(items) # spackt rum, today cashout wird zu oft angezeigt, liegt an filter in api.inventory
	return render_template("inventory.html", items=items, today_cashout=data["todays_cashout"], inventory_amount=data["inventory_amount"], url=f"/api/inventory/update/{steamid}"), 200
	#return jsonify(items)
	
@app.route("/test")
def test():
	#return requests.get("http://localhost:8080/api/inventory/refresh/76561198439884801").json
	return requests.post("http://localhost:8080/api/user", json={"steamkey": "123"}, headers={"Content-Type": "application/json"}).content # send get request with json body

if __name__ == "__main__":
	app.run(port=8080, debug=True, threaded=True)