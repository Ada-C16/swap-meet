CONDITIONS_DICTIONARY = {
    1: "Did the cat drag this in?", 
    2: "It has an aesthetic",
    3: "Perfectly adequate",
    4: "It's only been on the roller coaster once or twice",
    5: "OMG, UNBOXED"
}


class Item:
    """Instantiates an instance of an object - Item"""

    def __init__(self, category = "", condition = None):
        """Defines category of object as a black string unless passed in and condition as None unless a value 
        is passed in"""
        self.category = category
        self.condition = condition if condition else None
        
    def __str__(self):
        """Returns strong if condition is converted to string"""
        return "Hello World!"
    
    def condition_description(self):
        return CONDITIONS_DICTIONARY[self.condition]