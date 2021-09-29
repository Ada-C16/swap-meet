class Item:
    def __init__(self, category="", item_name="", id="Hello World!"):
        self.id = id
        self.category = category
        self.item_name = item_name
    
    def __str__(self):
        return str(self.id)
        

