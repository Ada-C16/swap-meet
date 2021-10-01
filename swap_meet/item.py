class Item:
    def __str__(self):
        return "Hello World!"

    def __init__(self, category= str(), condition =0, age =0):
        self.category = category
        self.condition = condition
        self.age = age        
    
    def condition_description(self):
        condition_message = ['Heavily used', 'Used', 'Used but in good conditon','Worn a few times - Great condition','like new - Great condition']
        return condition_message[round(self.condition -1)]