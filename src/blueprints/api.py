from flask import Blueprint, jsonify, request
import json
from urllib.request import urlopen
from steampy.client import SteamClient
from steampy.models import Currency, GameOptions
import time
import urllib
# IMPORTANT; Dieser teil wird nur einmal in der Nacht gecallt und NICHT vom frontend, das frontend callt nur die Datenbank api
api = Blueprint("api", __name__, url_prefix="/api")
steam_client = SteamClient("D13799E79A69DE038BB9A50AD1703129")

@api.route("/inventory/<steamid>")
def get_inventory(steamid):
    currency = "$"
    # TODO es muss ein Token übergeben werden, der diesen Teil autorisiert, wenn dieser nicht stimmt wird der teil nicht gecallt -> redirect zur db json call route
    # TODO neue Method erstellen die du Uhrzeit checkt und den Programm teil um 0:01 triggert ODER wenn es viele ids in der DB gibt, jede Stunde den programmteil mit einer anderen ID triggert (for loop durch die IDs) -> wenn Prozess fertig: Email an Nutzer.
    # TODO Nutzer kann sich sein INV in einem PDF doc runterladen (Items werden aufgeführt: `mengex Itemname`, am Ende steht der Heutige Cashout betrag, welcher auch auf den Startbildschirm des Nutzer (bei login stehen soll)) -> Aufbau wie bei einer Rechnung (FF; Unterschrift als joke am Ende)
    # TODO Advanced Function: item per Steam api verkaufen über eigenen API token, bei login muss der USer seinen eigenen Api token angeben: wenn login -> Programm benutzt diesen Api token!
    # TODO: check currency: if currency = EURO: currency=€
    #data = request.get_json() # TODO: steamid nicht über paramter übergeben, sondern über body dict
    #steamid = data["steam_id"]
    #currence = data["currency"]
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
                # TODO items dict in db speichern, dieser wird nur einmal am Tag gerefresht
        except:
            print("sleep...")
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

    return jsonify(items), 200 

    # TODO anuahl bekommt man mit der id eines items (sw-case: 519977179) und dann durch einen loop in rgInventory -> also einmal durch rgInventory loope, werte in einer liste speicher, diese werte zählen und dann den namen rausfinden