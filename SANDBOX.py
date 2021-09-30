
# --- WAVE ONE --- #

#      VENDOR      #


#vendor_has_inventory
#vendor_takes_optional_inventory
#adding_to_inventory
#removing_from_inventory_returns_item
#removing_not_found_is_false 



# --- WAVE TWO --- #

#      ITEMS       #


#items_have_blank_default_category 
#get_items_by_category
#get_no_matching_items_by_category



# --- WAVE THREE --- #

#     SWAP ITEMS     #


#item_overrides_to_string

#swap_items_returns_true

#swap_items_when_my_item_is_missing_returns_false
#swap_items_when_their_item_is_missing_returns_false

#swap_items_from_my_empty_returns_false
#swap_items_from_their_empty_returns_false



# --- WAVE FOUR --- #

#  SWAP FIRST ITEM  #


# first_item_returns_true


# swap_first_item_from_my_empty_returns_false
# swap_first_item_from_their_empty_returns_false



# --- WAVE FIVE --- #

#      CLOTHING     #


# clothing_has_default_category_and_to_str
# decor_has_default_category_and_to_str 
# electronics_has_default_category_and_to_str
# items_have_condition_as_float
# tems_have_condition_descriptions_that_are_the_same_regardless_of_type



# --- WAVE SIX --- #

# BEST BY CATEGORY #


# best_by_category
# best_by_category_no_matches_is_none
# best_by_category_with_duplicates

# swap_best_by_category
# swap_best_by_category_reordered
# swap_best_by_category_no_inventory_is_false
# swap_best_by_category_no_other_inventory_is_false
# swap_best_by_category_no_match_is_false
# swap_best_by_category_no_other_match_is_false