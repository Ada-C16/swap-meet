class Item:
    def __init__(self, category = None, condition = 0.0):
        if not category:
            category = ''
        self.category = category
        self.condition = condition

    def __str__(self, description = 'Hello World!'):
        return description

    def condition_description(self):
        return f'The item condition is {self.condition}.'
