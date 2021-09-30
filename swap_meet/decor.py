class Decor:
    def __init__(self, category="Decor", condition=0, id="Something to decorate your space."):
        self.category = category
        self.id = id
        self. condition = condition

    def __str__(self):
        return str(self.id)
