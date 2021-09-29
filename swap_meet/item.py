
class Item():
    def __init__(self, category = "", condition=0, age=0):
        self.category = category
        self.condition = condition 
        self.age = age

    def __str__(self):
        return ("Hello World!")

    def condition_description(self):
        if self.condition <= 2:
            return "used - normal"
        elif self.condition <= 3:
            return "good"
        elif self.condition <= 4:
            return "heavily used"
        else:
            return "mint"