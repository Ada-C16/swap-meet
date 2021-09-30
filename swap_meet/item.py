class Item:
    def __init__(self, category = None, condition = 0.0, age = 0):
        self.category = category if category else ''
        self.condition = condition
        self.age = age

    def __str__(self, description = 'Hello World!'):
        return description

    def condition_description(self):
        return f'The item condition is {self.condition}.'
