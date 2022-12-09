from CashRegister import CashRegister
from Dispenser import Dispenser

class CandyMachine:
    """candy machine"""
    def __init__(self):
        self.candy = Dispenser()
        self.chips = Dispenser()
        self.gum = Dispenser()
        self.cookies = Dispenser()

    def showSelection(self):
        """displays the menu"""
        banner1 = "Welcome to Sweet's Candy Shop".center(4,"*")
        banner2 =\
"""
To select an item enter
1 for Candy
2 for Chips
3 for Gum
4 for Cookies
0 to View Balance
9 to Exit
"""
        print(banner1, banner2)

    def sellProduct(self, product, cRegister):
        # must have dispenser
        # check whether dispenser is empty; sold out
        # tells amount to buy product
        # decrement dispenser size and update cash reg
        # return cash changes

        pass
