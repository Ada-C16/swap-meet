


class Item:#might have to chage and add the conditional
    def __init__(self, category="", condition = 0):

        self.category=category
        self.condition=condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        # return f"{self.condition}"
        if self.condition > 0 and self.condition < 1: 
            return "hello"
        elif self.condition ==1:
            return "sup"
        elif self.condition==2:
            return "what up"
        elif self.condition ==3:
            return "hola"
        elif self.condition ==4:
            return "whats good"
        elif self.condition ==5:
            return "yo"
        else:
            return "yo invalid"