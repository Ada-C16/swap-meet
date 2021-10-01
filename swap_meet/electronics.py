from .item import Item


class Electronics(Item):
    """
    An electronics subclass of the Item class
    Attributes:
        name: a string that is the name of the item
        condition: an int from 0-5 representing the condition of the item
        age: an int representing how many years old the item is
        category: a string matching "Electronics"
    """

    def __init__(self, name="", condition=0, age=None):
        """
        Parameters:
            name: a string that is the name of the item
            condition: an int from 0-5 representing the condition of the item
            age: an int representing how many years old the item is
        """
        super().__init__(name, condition, age, category="Electronics")

    def __str__(self):
        return "A gadget full of buttons and secrets."
