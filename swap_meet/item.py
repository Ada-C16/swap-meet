class Item:
    def __init__(self, category = None, condition = 0.0, age = 0):
        self.category = category if category else ''
        self.condition = condition
        self.age = age

    def __str__(self, description = 'Hello World!'):
        return description

    def condition_description(self):
        CONDITION_STATEMENTS = {
            0: 'Probably it has no rating yet',
            1: 'We blame bad service',
            2: 'Barely acceptable',
            3: 'Average',
            4: 'Great product, and great service',
            5: 'Paid reviews',
            6: 'Rating value out of bound'
        }
        condition_statement = CONDITION_STATEMENTS[6]
        if self.condition <= 0.5:
            condition_statement = CONDITION_STATEMENTS[0]
        elif self.condition <= 1.5:
            condition_statement = CONDITION_STATEMENTS[1]
        elif self.condition <= 2.5:
            condition_statement = CONDITION_STATEMENTS[2]
        elif self.condition <= 3.5:
            condition_statement = CONDITION_STATEMENTS[3]
        elif self.condition <= 4.5:
            condition_statement = CONDITION_STATEMENTS[4]
        elif self.condition <= 5.0:
            condition_statement = CONDITION_STATEMENTS[5]

        return condition_statement
