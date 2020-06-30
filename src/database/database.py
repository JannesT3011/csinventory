from pymongo import MongoClient
import pymongo
from datetime import datetime
import json
# mpngodb oder sql
# TODO: inventarwerte wird in einer Tablle mit primary key steamid gespeichert , andere werte zum einloggen in die USER table!
# TODO error loggen und auf extra route speichern
"""
LAYOUT:
USER (login with steam)
- email
- other stuff from steam

INVENTORY
steamid primary key,
inv: dict           api response
value: int          total value of inventory
"""

with open("config.json") as cf:
    config = json.load(cf)

class Database:
    def __init__(self):
        self.inventory_db_name = config["inventory_db_name"]
        self.user_db_name = config["user_db_name"]
        self.config_db_name = config["config_db_name"]
        self.cluster = MongoClient(config["mongodb_link"])
        self.db = self.cluster[config["cluster"]]
    
    def execute(self, collection:str):
        if collection in [self.inventory_db_name, self.user_db_name, self.config_db_name]:
            self.collection = self.db[collection]
            return self.collection
        else:
            return "No collection selected"

    def init_inventory_db(self, steamid: str):
        try:
            return self.execute(self.inventory_db_name).insert_one(self.inventory_layout(steamid))
        except:
            #raise pymongo.errors.DuplicateKeyError("SteamID is already registered")
            raise
    def init_user_db(self, steamkey):
        try:
            return self.execute(self.user_db_name).insert_one(self.user_layout(steamkey))
        except:
            raise pymongo.errors.DuplicateKeyError("Steamkey is already registered")
    
    def init_config_db(self):
        try:
            return self.execute(self.config_db_name).insert_one(self.config_layout).encode("utf-8")
        except:
            raise pymongo.errors.DuplicateKeyError("Config table already created!")

    def delete_inventory_db(self, steamid:str):
        try:
            return self.execute(self.inventory_db_name).delete_one({"_id": steamid})
        except:
            raise

    def delete_user_db(self, steamkey):
        try:
            return self.execute(self.user_db_name).delete_one({"_id": steamkey})
        except:
            raise
    
    def delete_config_db(self):
        try:
            return self.execute(self.config_db_name).delete_one({"_id": "_config"})
        except:
            raise
    
    @classmethod
    def inventory_layout(cls, steamid:str) -> dict:
        return {
            "_id": steamid,
            "inv": {},
            "last_refresh": "",
            "history": {},
            "created_at": datetime.utcnow()
        }
    
    @classmethod
    def user_layout(cls, steamkey) -> dict:
        return {
            "_id": steamkey,
            "email": "",
            "name": "",
            "steam_api_token": "",
            "api_key": "",
            "joined_at": datetime.utcnow()
        }
    
    @classmethod
    def config_layout(cls) -> dict:
        return {
            "_id": "_config",
            "steam_api_tokens": [],
            "api_key": {} # name: api_key
        }
if __name__ == "__main__":
    db = Database()
    db.execute("inventory").update_one({"_id":"123"}, {"$set": {"inv": {"test":"dwdwd"}}})