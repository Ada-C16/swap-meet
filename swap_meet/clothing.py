class Clothing:
    def __init__(self, category="Clothing", condition=0, id="The finest clothing you could wear."):
        self.category = category
        self.id = id
        self. condition = condition
    
    def __str__(self):
        return str(self.id)
