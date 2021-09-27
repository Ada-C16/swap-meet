from .item import Item

class Electronics(Item):
    def __init__(self, descrip="A gadget full of buttons and secrets.", category="Electronics", condition=None):
        super().__init__(descrip=descrip,category=category,condition=condition)
