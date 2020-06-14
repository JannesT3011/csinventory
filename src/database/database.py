from pymongo import MongoClient
import pymongo
from datetime import datetime
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

class Database:
    def __init__(self):
        self.cluster = MongoClient("CONNECTION")
        self.db = self.cluster["CLUSTER"]
        self.collection = self.db["DB"]
    
    def __call__(self):
        return self.collection

    def init_inventory_db(self, steamid: str):
        try:
            return self.collection.insert_one(self.inventory_layout(steamid))
        except:
            raise pymongo.errors.DuplicateKeyError("SteamID is already registered")

    def init_user_db(self, steamkey):
        try:
            return self.collection.insert_one(self.user_layout(steamkey))
        except:
            raise pymongo.errors.DuplicateKeyError("Steamkey is already registered")
    
    def init_config_db(self):
        try:
            return self.collection.insert_one(self.config_layout)
        except:
            raise pymongo.errors.DuplicateKeyError("Config table already created!")

    def delete_inventory_db(self, steamid:str):
        try:
            return self.collection.delete_one({"_id": steamid})
        except:
            raise

    def delete_user_db(self, steamkey):
        try:
            return self.collection.delete_one({"_id": steamkey})
        except:
            raise
    
    def delete_config_db(self):
        try:
            return self.collection.delete_one({"_id": "_config"})
        except:
            raise
    
    @classmethod
    def inventory_layout(cls, steamid:str) -> dict:
        return {
            "_id": steamid,
            "inv": dict,
            "last_refresh": str
            "created_at": datetime.utcnow()
        }
    
    @classmethod
    def user_layout(cls, steamkey) -> dict:
        return {
            "_id": steamkey,
            "email": str
            "name": str,
            "api_token": str,
            "joined_at": datetime.utcnow()
        }
    
    @classmethod
    def config_layout(cls) -> dict:
        return {
            "_id": "_config",
            "api_tokens": list
        }