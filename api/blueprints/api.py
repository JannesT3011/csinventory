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
from csinventorypy import CSInventory

with open("config.json") as cf:
    config = json.load(cf)

api = Blueprint("api", __name__, url_prefix="/api")
steam_client = SteamClient(config["steam_apikey"])
db = Database()
API_KEY = config["secret_api_key"]


# INVENTORY ROUTES

@api.route("/inventory/refresh/<steamid>", methods=["GET", "POST"])
def refresh_inventory(steamid, triggeredFromCode:bool=False) -> jsonify:
    if not triggeredFromCode:
        data = request.get_json()
        try:
            api_key = data["api_key"]
        except KeyError:
            return jsonify({"message": "Bad Request"}), 400
        if api_key != API_KEY:
            return jsonify({"message": "You are not authorized!"}), 401
    #steamid = request.get_json()["steamid"]
    currency = "$"

    items = CSInventory(steamid).get_inv_steamdata(config["steam_apikey"], False) 

    all_totals = []
    all_cashouts = []
    all_amounts = []

    for it in items:
        try:
            all_totals.append(items[it]["total_median"])
            all_cashouts.append(items[it]["total_cashout"])
            all_amounts.append(items[it]["amount"])
        except KeyError:
            all_totals.append(0)
            all_cashouts.append(0)
    total_inv_value = sum(all_totals)
    today_cashout = sum(all_cashouts)
    items["inventory_amount"] = sum(all_amounts)
    items["inventory_value_median"] = f"{currency}{round(total_inv_value, 2)}"
    items["todays_cashout"] = f"{currency}{round(today_cashout, 2)}"
    
    try:
        db.init_inventory_db(steamid)
        db.execute("inventory").update_one({"_id":steamid}, {"$set": {"inv": items}}) 
        db.execute("inventory").update_one({"_id":steamid}, {"$set": {"history."+current(): items}}) 
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


@api.route("/inventory", methods=["POST"])
def get_inventory():
    data = request.get_json()
    try:
        steamid = data["steamid"]
        update = data["update"]
        api_key = data["api_key"]
    except KeyError:
        return jsonify({"message": "Bad Request"}), 400
    if api_key != API_KEY:
        return jsonify({"message": "You are not authorized!"}), 401

    if update:
        result = refresh_inventory(steamid)
    else:
        try:
            result = db.execute("inventory").find_one({"_id":steamid})
            last_refresh = result["last_refresh"]
            delta = datetime.strptime(current(), "%Y-%m-%d %H:%M:%S") - datetime.strptime(result["last_refresh"], "%Y-%m-%d %H:%M:%S")
            if result["inv"] == {}:
                result = refresh_inventory(steamid)
            elif "day," in str(delta).split(" "):
                result = refresh_inventory(steamid)
            else:
                result = result["inv"]
                result["last_refresh"] = last_refresh
        except:
            result = refresh_inventory(steamid)
    try:
        return jsonify(result["inv"]), 200
    except KeyError:
        return jsonify(result), 200

@api.route("/inventory/delete")
def delete_inventory() -> jsonify:
    data = request.get_json()
    try:
        steamid = data["steamid"]
        api_key = data["api_key"]
    except KeyError:
        return jsonify({"message": "Bad Request"}), 400
    if api_key != API_KEY:
        return jsonify({"message": "You are not authorized!"}), 401

    try:
        db.execute("inventory").delete_one({"_id":steamid})
    except:
        return jsonify({"msg": "Error"}), 400
    
    return jsonify({"msg": f"{steamid} deleted!"}), 200

@api.route("/inventory/history", methods=["POST"])
def history_inventory() -> jsonify:
    data = request.get_json()
    try:
        steamid = data["steamid"]
        api_key = data["api_key"]
    except KeyError:
        return jsonify({"message": "Bad Request"}), 400
    if api_key != API_KEY:
        return jsonify({"message": "You are not authorized!"}), 401
    try:
        result = db.execute("inventory").find_one({"_id":steamid})
        return jsonify(result["history"]),200
    except:
        raise

@api.route("/inventory/stats", methods=["POST"])
def inventory_stats():
    data = request.get_json()
    try:
        steamid = data["steamid"]
        api_key = data["api_key"]
    except KeyError:
        return jsonify({"message": "Bad Request"}), 400
    if api_key != API_KEY:
        return jsonify({"message": "You are not authorized!"}), 401

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