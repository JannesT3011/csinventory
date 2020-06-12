from flask import Blueprint, jsonify, request
import json
from urllib.request import urlopen
from steampy.client import SteamClient
from steampy.utils import GameOptions
import time

api = Blueprint("api", __name__, url_prefix="/api")
steam_client = SteamClient("")

@api.route("/inventory/<steamid>")
def get_inventory(steamid):
    #data = request.get_json()
    #steamid = data["steam_id"]
    data = urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
    json_data = json.loads(data.read())
    descriptions = json_data['rgDescriptions']
    inv =  [descriptions[v]['market_hash_name'] for v in descriptions]
    x = {}
    for item in inv:
        try:
            if item.startswith("Sealed") or item.startswith("Graffiti") or item.endswith("Medal"):
                pass
            else:
                x[item] = steam_client.market.fetch_price(item, GameOptions.CS)
        except:
            time.sleep(60)
    print(x)

    return jsonify(x), 200 # TODO geht!, aber nur x returnen

    # TODO anuahl bekommt man mit der id eines items (sw-case: 519977179) und dann durch einen loop in rgInventory -> also einmal durch rgInventory loope, werte in einer liste speicher, diese werte zählen und dann den namen rausfinden