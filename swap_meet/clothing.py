from .item import Item

class Clothing(Item):
    # new init method with new paramaters
    def __init__(self, category = "", condition = None):
    # def __init__(self, category, condition):
        # call superclass' constructor
        # super().__init__(category = "", condition = None)
        super().__init__(category, condition)
        self.category = "Clothing"

    # def __init__(self, condition, category = ""):
    #     Item.__init__(self, category, condition)
    #     self.category = "clothing"
    # #     self.category = category

    def __str__(self):
        return "The finest clothing you could wear."
