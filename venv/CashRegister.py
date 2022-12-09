# built in cash register

class CashRegister:
    """monitors machine balances in every transaction"""

    # default 500 cents
    def __init__(self, cashOnHand=500):
        """def values on cash reg"""

        if cashOnHand <= 0:
            cashOnHand = 500
        else:
            self.cashOnHand = cashOnHand #on cents

    # gets balance
    def currentBalance(self):
        """gets current balance"""
        return self.cashOnHand

    def acceptAmount(self, amount):
        """increment cashonhand"""
        self.cashOnHand += amount

if __name__ == '__main__':
    print("CashRegister.py is main(). Default values is:")
    cashreg = CashRegister()
    print("cashonhand: ", cashreg.currentBalance())
    print("accepts amount of 200; new value: ", cashreg.acceptAmount(200))
