from datetime import datetime

class User(object): # login required -> see more data
    def __init__(self, email:str, name:str, api_token:str, joined_at:datetime):
        self.email = email
        self.name = name
        self.api_token = api_token
        self.joined_at = joined_at