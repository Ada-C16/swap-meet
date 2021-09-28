#WAVE 02
# [X] For Tests 1-3
#     [X] Each Item will have an attribute named category, which is an empty 
#         string by default
#     [X] When we initialize an instance of Item, we can optionally pass in a 
#         string with the keyword argument category
#     [X] Instances of Vendor have an instance method named get_by_category
#           [X] It takes one argument: a string, representing a category  
#           [X] This method returns a list of Items in the inventory with 
#               that category  

#WAVE 03
# [ ] For Test 1
#     [ ] When we stringify (convert to a string) an instance of Item using str(), 
#         it returns "Hello World!" 
#           [ ] This implies Item overrides its stringify method. We may need to 
#               research the __str__ method for more details! 
# [X] For Tests 2-6
#     [X] Instances of Vendor have an instance method named swap_items. 
#         It takes 3 arguments:
#           [X] an instance of another Vendor, representing the friend that the 
#               vendor is swapping with
#           [X] an instance of an Item (my_item), representing the item this 
#               Vendor instance plans to give 
#           [X] an instance of an Item (their_item), representing the item the 
#               friend Vendor plans to give 
#     [X] It removes the my_item from this Vendor's inventory, and adds it to the 
#         friend's inventory 
#     [X] It removes the their_item from the other Vendor's inventory, and adds it 
#         to this Vendor's inventory
#     [X] It returns True 
#     [X] If this Vendor's inventory doesn't contain my_item or the friend's 
#         inventory doesn't contain their_item, the method returns False


class Item:
    def __init__(self, category = None):
        if not category:
            category = ""
        self.category = category

    
