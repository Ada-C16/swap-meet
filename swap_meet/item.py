class Item:
    """
    A class for an item.
    Attributes:
        name: a string that is the name of the item
        condition: an int from 0-5 representing the condition of the item
        age: an int representing how many years old the item is
        category: a string that is the category of the item
    """

    def __init__(self, name="", condition=0, age=None, category=""):
        """
        Constructor for class Item
        Parameters:
            name: a string that is the name of the item
            condition: an int from 1-5 representing the condition of the item
            age: an int representing how many years old the item is
            category: a string that is the category of the item
        """
        self.name = name
        self.category = category
        self.condition = condition
        self.age = age

    def condition_description(self):
        """
        Result:
            Returns a description of the condition based on the numerical self.condition rating
        """
        condition_descriptions = {
            5: "Top of the line, there's nothing like this out there",
            4: "Pretty great but there may be a couple microscratches, bent corners, etc",
            3: "Just your run of the mill item, nothing special here",
            2: "I mean it *probably* works? Right?",
            1: "This is being traded for parts",
            0: "No one remembered to update the condition, so we have no idea!",
        }
        return condition_descriptions[int(self.condition)]

    def __str__(self):
        return "Hello World!"
