discount_pirce_condition_dict = {
                                        5 : 1, 
                                        4 : 0.80,
                                        3 : 0.60,
                                        2 : 0.40,
                                        1 : 0.20,
                                        0 : 0,
                                        }
def swap_by_most_valuable_with_discount_on_condition(self, other):
    my_discounted_price_inventory_list = []
    for each_item in self.inventory:
        my_discounted_price_inventory_list.append(each_item.price * self.discount_price_condition_dict[each_item.condition])
    
    their_discounted_price_inventory_list = []
    for each_item in other.inventory:
        their_discounted_price_inventory_list.append(each_item.price * other.discount_price_condition_dict[each_item.condition])
        