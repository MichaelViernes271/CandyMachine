from CashRegister import CashRegister
from Dispenser import Dispenser

class CandyMachine:
    """candy machine"""
    def __init__(self):

        # items in dispenser
        self.candy = Dispenser(cost=1)
        self.chips = Dispenser(cost=2)
        self.gum = Dispenser(cost=3)
        self.cookies = Dispenser(cost=4)
        # cashregister
        self.cashreg = CashRegister()

    def showSelection(self):
        """displays the menu"""
        banner1 = "Welcome to Sweet's Candy Shop".center(50,"*")
        banner2 = \
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

        # while True:
        #     # gathering orders from user till it exits
        #     # prints display menu
        #
        #     try:
        #         usr_input = int(input("Enter your choice: "))
        #         if ((usr_input > 4 and usr_input < 9) or (usr_input < 0 or usr_input > 9 )):
        #             raise ValueError
        #     except:
        #         print("Bad choice here. Try again.")
        #
        #     if (usr_input == 0):
        #         print("exiting...")
        #         exit()
        #
        #     if (usr_input == 1):
        #         cashchange = self.sellProduct(self.candy, self.cashreg)
        #         if not cashchange:
        #             print(f"You bought a cookie. Your change is {cashchange}.\n")


    def sellProduct(self, product, cRegister):
        # must have dispenser
        # check whether dispenser is empty; sold out
        # tells amount to buy product
        # decrement dispenser size and update cash reg
        # return cash changes
        if not (product.getCount()):
            print("SOLD OUT!".center(50, "*"))
            return
        else:
            print(f"The product costs {product.getProductCost()}.")
            while True:
                try:
                    usr_amount = int(input("Enter amount or 0 to cancel: "))
                    if usr_amount == 0:
                        return
                    assert (usr_amount >= product.getProductCost()) or (usr_amount > 0)
                    break
                except:
                    print("You must have insufficient money. Try Again.\n")

            # processing user amount to the particular dispenser and stores cash on register
            cRegister.acceptAmount(usr_amount)
            product.makeSale()
            print(f"Remaining items: {product.getCount()}")

            # return cash change if any
            cashchange = usr_amount - product.cost
            print(f"You bought an item. Your change is {cashchange}.\n")
            return cashchange
