from swap_meet.item import Item


from .item import Item


class Clothing(Item):
    """
    A clothing subclass of the Item class
    Attributes:
        name: a string that is the name of the item
        condition: an int from 0-5 representing the condition of the item
        age: an int representing how many years old the item is
        category: a string matching "Clothing"
    """

    def __init__(self, name="", condition=0, age=None):
        """
        Parameters:
            name: a string that is the name of the item
            condition: an int from 0-5 representing the condition of the item
            age: an int representing how many years old the item is
        """
        super().__init__(name, condition, age, category="Clothing")

    def __str__(self):
        return "The finest clothing you could wear."
