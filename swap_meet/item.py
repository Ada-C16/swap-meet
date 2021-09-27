class Item:
    def __str__(self) -> str:
        return self.name
    def __init__(self, name=None, category=None):
        self.name = name or "Hello World!"
        self.category = category or ""