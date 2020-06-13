from flask_sqlalchemy import sqlalchemy
# mpngodb oder sql
# TODO: inventarwerte wird in einer Tablle mit primary key steamid gespeichert , andere werte zum einloggen in die USER table!

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
    pass