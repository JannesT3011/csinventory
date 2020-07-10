from flask import Blueprint, jsonify, request, redirect, url_for
import json
from urllib.request import urlopen
from steampy.client import SteamClient
from steampy.models import Currency, GameOptions
import time
import urllib
from ..database import Database
import pymongo
from datetime import datetime
from ..utils.current_time import current
import json

with open("config.json") as cf:
    config = json.load(cf)

# IMPORTANT; Dieser teil wird nur einmal in der Nacht gecallt und NICHT vom frontend, das frontend callt nur die Datenbank api
api = Blueprint("api", __name__, url_prefix="/api")
steam_client = SteamClient(config["steam_apikey"])
db = Database()
# INVENTORY ROUTES

@api.route("/inventory/refresh/<steamid>", methods=["GET", "POST"])
def refresh_inventory(steamid) -> jsonify:
    #steamid = request.get_json()["steamid"]
    currency = "$"
    # TODO es muss ein Token übergeben werden, der diesen Teil autorisiert, wenn dieser nicht stimmt wird der teil nicht gecallt -> redirect zur db json call route
    # TODO neue Method erstellen die du Uhrzeit checkt und den Programm teil um 0:01 triggert ODER wenn es viele ids in der DB gibt, jede Stunde den programmteil mit einer anderen ID triggert (for loop durch die IDs) -> wenn Prozess fertig: Email an Nutzer.
    # TODO Nutzer kann sich sein INV in einem PDF doc runterladen (Items werden aufgeführt: `mengex Itemname`, am Ende steht der Heutige Cashout betrag, welcher auch auf den Startbildschirm des Nutzer (bei login stehen soll)) -> Aufbau wie bei einer Rechnung (FF; Unterschrift als joke am Ende)
    # TODO Advanced Function: item per Steam api verkaufen über eigenen API token, bei login muss der USer seinen eigenen Api token angeben: wenn login -> Programm benutzt diesen Api token!
    # TODO: check currency: if currency = EURO: currency=€
    #data = request.get_json() # TODO: steamid nicht über paramter übergeben, sondern über body dict
    #steamid = data["steam_id"]
    #currence = data["currency"] 
    # TODO es wird nicht jedes item gezählt (es werden welche ausgelassen) -> neu testen
    try:
        data = urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
    except:
        time.sleep(60)
        refresh_inventory(steamid)

    json_data = json.loads(data.read())
    descriptions = json_data['rgDescriptions']
    inv =  [descriptions[v] for v in descriptions]

    items = {}
    number_inv = []
    amount = {}

    for value in json_data["rgInventory"]:
        number_inv.append(json_data["rgInventory"][value]["classid"]) # TODO key class id benutzen! nochmal die row json angucken
    
    for iid in number_inv:
        amount[iid] = number_inv.count(iid)
    
    for item in inv:
        item_ = item["market_hash_name"]
        try:
            if item_.startswith("Sealed") or item_.startswith("Graffiti") or item_.endswith("Medal") or item_.startswith("Storage") or item_.endswith("Badge"):
                pass
            else:
                steam_info = steam_client.market.fetch_price(item_, GameOptions.CS) #TODO currency ändern .replace(§(und das 'USd'), currency)
                items[item_] = steam_info # die möglichkeit in euro umzurechnen
                items[item_]["amount"] = amount[item["classid"]]
                items[item_]["total_median"] = f'${round(items[item_]["amount"] * float(steam_info["median_price"].split(" USD")[0].split("$")[1]), 2)}'
                items[item_]["total_cashout"] = f'${round(items[item_]["amount"] * float(steam_info["lowest_price"].split(" USD")[0].split("$")[1]), 2)}'
                items[item_]["buy_price"] = "0"
                items[item_]["total_buy_price"] = "0"
        except:
            time.sleep(60)
            
    all_totals = []
    all_cashouts = []
    all_amounts = []

    for it in items:
        all_totals.append(float(items[it]["total_median"].split(currency)[1]))
        all_cashouts.append(float(items[it]["total_cashout"].split(currency)[1]))
        all_amounts.append(items[it]["amount"])
    total_inv_value = sum(all_totals)
    today_cashout = sum(all_cashouts)
    items["inventory_amount"] = sum(all_amounts)
    items["inventory_value_median"] = f"{currency}{round(total_inv_value, 2)}"
    items["todays_cashout"] = f"{currency}{round(today_cashout, 2)}"
    
    try:
        db.init_inventory_db(steamid)
        db.execute("inventory").update_one({"_id":steamid}, {"$set": {"inv": items}}) 
        db.execute("inventory").update_one({"_id":steamid}, {"$set": {"history."+current(): items}}) # TODO time muss string sein
        db.execute("inventory").update_one({"_id":steamid}, {"$set": {"last_refresh": current()}})
        return items
    except pymongo.errors.DuplicateKeyError:
        try: 
            db.execute("inventory").update_one({"_id":steamid}, {"$set": {"inv": items}})
            db.execute("inventory").update_one({"_id":steamid}, {"$set": {"history."+current(): items}})
            db.execute("inventory").update_one({"_id":steamid}, {"$set": {"last_refresh": current()}})
            return items
        except:
            raise
    else:
        return items


@api.route("/inventory", methods=["POST"]) # TODO beim resfresh gibt es einen fehler, keine json data erkannt
def get_inventory():
    data = request.get_json()
    steamid = data["steamid"]
    update = data["update"]
    if update:
        result = refresh_inventory(steamid)
    else:
        try:
            result = db.execute("inventory").find_one({"_id":steamid})
            delta = datetime.strptime(current(), "%Y-%m-%d %H:%M:%S") - datetime.strptime(result["last_refresh"], "%Y-%m-%d %H:%M:%S")
            if result["inv"] == {}:
                result = refresh_inventory(steamid)
            elif "day," in str(delta).split(" "):
                result = refresh_inventory(steamid)
            else:
                result = result["inv"]
        except:
            result = refresh_inventory(steamid)
    try:
        return jsonify(result["inv"]), 200
    except KeyError:
        return jsonify(result), 200

@api.route("/inventory/delete")
def delete_inventory() -> jsonify:
    data = request.get_json()
    steamid = data["steamid"]
    try:
        db.execute("inventory").delete_one({"_id":steamid})
    except:
        return jsonify({"msg": "Error"}), 400
    
    return jsonify({"msg": f"{steamid} deleted!"}), 200

@api.route("/inventory/history", methods=["POST"])
def history_inventory() -> jsonify:
    data = request.get_json()
    steamid = data["steamid"]
    try:
        result = db.execute("inventory").find_one({"_id":steamid})
        return jsonify(result["history"]),200
    except:
        raise

@api.route("/inventory/stats", methods=["POST"])
def inventory_stats():
    data = request.get_json()
    steamid = data["steamid"]
    try:
        result = db.execute("inventory").find_one({"_id": steamid})["history"]
        results = {}
        for date in result:
            results[date] = {}
            for i in result[date]:
                if i == "inventory_amount" or i == "todays_cashout" or i == "inventory_value_median":
                    results[date]["inventory_amount"] = result[date]["inventory_amount"]
                    results[date]["todays_cashout"] = result[date]["todays_cashout"]
                    results[date]["inventory_value_median"] = result[date]["inventory_value_median"]

        return jsonify(results), 200
    except:
        raise

# USER ROUTES
@api.route("/user", methods=["POST"])
def get_user() -> jsonify:
    data = request.get_json()
    steamkey = data["steamkey"]
    return steamkey

@api.route("/user/update")
def update_user() -> jsonify:
    return

@api.route("/user/delete")
def delete_user() -> jsonify:
    return

@api.route("/user/new")
def new_user():
    return

@api.route("/user/send_mail")
def send_mail_user() -> jsonify:
    return

def get_api_key():
    return db.execute("config").find({"_id": "_config"})["api_key"]