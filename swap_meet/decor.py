from .item import Item

class Decor(Item):
    def __init__(self, descrip="Something to decorate your space.", category="Decor", condition=None):
        super().__init__(descrip=descrip,category=category,condition=condition)
