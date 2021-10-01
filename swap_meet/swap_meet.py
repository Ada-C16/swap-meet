from .vendor import Vendor


class SwapMeet:
    """
    A class to run the swap meet
    Attributes:
        vendors: a list of Vendor objects
    """

    def __init__(self, vendors=None):
        """
        Constructor for SwapMeet class
        Parameters:
            vendors: a list of Vendor objects
        """
        self.vendors = vendors if vendors else []

    @staticmethod
    def print_welcome():
        """
        Result:
            prints welcome messages/starts off the swap meet
        """
        print("******************************")
        print("\nWelcome to the Swap Meet!\n")
        print("******************************")
        print("\nMeet our vendors:\n")

    def print_vendor_inventories(self):
        """
        Result:
            prints out the inventories of each vendor in self.vendors
        """
        for vendor in self.vendors:
            vendor.print_inventory()
            print("\n******************************\n")

    @staticmethod
    def get_swap_type():
        """
        Result:
            Returns a number 1, 2, or 3 based on the user's choice of swap type
        """
        print(
            "Do you want to: \n\
        1. Swap the two newest items from each vendor's inventory? \n\
        2. Swap the first items from each vendor's inventory? \n\
        3. Swap the the 2 best by items by certain categories?"
        )

        option = int(input("Choose a number from above.\n"))
        return option

    @staticmethod
    def get_category_options(vendor):
        """
        Parameter:
            vendor: a Vendor object
        Result:
            Returns a string matching the category the user chooses
        """
        print(
            "\nCategories: \n\
        1. misc \n\
        2. clothing\n\
        3. electronics\n\
        4. decor"
        )

        category = int(
            input(
                f"Choose a number from above to pick the category that {vendor.name} wants to recieve.\n"
            )
        )

        if category == 1:
            return "misc"
        elif category == 2:
            return "Clothing"
        elif category == 3:
            return "Electronics"
        elif category == 4:
            return "Decor"
