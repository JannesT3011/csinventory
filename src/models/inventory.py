

class Inventory(object): # no login required -> only see inventory value, total_value and total_value graph
    def __init__(self, items:dict, total_value:int):
        self.items = items
        self.total_value = total_value