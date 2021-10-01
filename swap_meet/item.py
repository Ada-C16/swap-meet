class Item:
    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return ("Hello World!")

    # Wave 5
    """This method evaluates the the 
      condition of each item 
      and prints out a message based 
      on the condition of each item.
      """
    def condition_description(self):
        if self.condition == 0:
            return("It's one of a kind :)")
        elif self.condition == 1:
            return("I hope you are handy!")
        elif self.condition == 2:
            return("Almost New - sort of!")
        elif self.condition == 3:
            return("A bang for your buck")
        elif self.condition == 4:
            return("It's pratically new")
        elif self.condition == 5:
            return("This is a STEAL!")
