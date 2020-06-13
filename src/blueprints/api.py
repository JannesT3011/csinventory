from flask import Blueprint, jsonify, request
import json
from urllib.request import urlopen
from steampy.client import SteamClient
#from steampy.utils import GameOptions
from steampy.models import Currency, GameOptions
import time
import urllib

api = Blueprint("api", __name__, url_prefix="/api")
steam_client = SteamClient("D13799E79A69DE038BB9A50AD1703129")

@api.route("/inventory/<steamid>")
def get_inventory(steamid):
    #data = request.get_json()
    #steamid = data["steam_id"]
    data = urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
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
    #print(amount)
    for item in inv:
        item_ = item["market_hash_name"]
        try:
            if item_.startswith("Sealed") or item_.startswith("Graffiti") or item_.endswith("Medal") or item_.startswith("Storage") or item_.endswith("Badge"):
                pass
            else:
                #items[item_]["amount"] = amount[item["classid"]]
                #print(item["classid"])
                items[item_] = steam_client.market.fetch_price(item_, GameOptions.CS, currency=Currency.EURO) # die möglichkeit in euro umzurechnen
                items[item_]["amount"] = amount[item["classid"]]
                # TODO items dict in db speichern, dieser wird nur einmal am Tag gerefresht
        except:
            print("sleep...")
            time.sleep(60)
            #print(e)
            
    #print(x)

    return jsonify(items), 200 # TODO geht!, aber nur x returnen

    # TODO anuahl bekommt man mit der id eines items (sw-case: 519977179) und dann durch einen loop in rgInventory -> also einmal durch rgInventory loope, werte in einer liste speicher, diese werte zählen und dann den namen rausfinden