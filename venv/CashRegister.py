# built in cash register

class CashRegister:
    """monitors machine balances in every transaction"""

    # default 500 cents
    def __init__(self, cashOnHand=500):

        if cashOnHand <= 0:
            self.cashOnHand = 500
        else:
            self.cashOnHand = cashOnHand #on cents

    # gets balance
    def currentBalance(self):
        return self.cashOnHand

    # increment cashonhand
    def acceptAmount(self, amount):
        self.cashOnHand += amount

if __name__ == '__main__':
    print("CashRegister.py is main(). Default values is:")
    cashreg = CashRegister()
    print("cashonhand: ", cashreg.currentBalance())
    print("accepts amount of 200; new value: ", cashreg.acceptAmount(200))
