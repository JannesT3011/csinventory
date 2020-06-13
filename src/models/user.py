from datetime import datetime

class User(object): # login required -> see more data
    def __init__(self, email:str, name:str, joined_at: datetime):
        self.email = email
        self.name = name
        self.joined_at = joined_at