from .item import Item

class Clothing(Item):
    def __init__(self, descrip="The finest clothing you could wear.", category="Clothing", condition=None):
        super().__init__(descrip=descrip,category=category,condition=condition)
