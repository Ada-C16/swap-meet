class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """This method describes the condition in words based on the value 0-5."""

        if self.condition <= 1:
            return("super used don't buy it")
        elif self.condition <= 2:
            return("pretty worn")
        elif self.condition  <=3:
            return("it's good for a date")
        elif self.condition <=4:
            return("Absolutely worth it")
        elif self.condition <=5:
            return("You bought it! YAY")

"""Final Submission"""