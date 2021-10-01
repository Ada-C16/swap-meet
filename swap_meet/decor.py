from .item import Item


class Decor(Item):
    """
    A decor subclass if the Item class
    Attributes:
        name: a string that is the name of the item
        condition: an int from 0-5 representing the condition of the item
        age: an int representing how many years old the item is
        category: a string matching "Decor"
    """

    def __init__(self, name="", condition=0, age=None):
        """
        constuctor for Decor class
        Parameters:
            name: a string that is the name of the item
            condition: an int from 0-5 representing the condition of the item
            age: an int representing how many years old the item is
        """
        super().__init__(name, condition, age, category="Decor")

    def __str__(self):
        return "Something to decorate your space."
