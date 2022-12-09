# Objective:
# The program should do the following:
# 1. Show the customer the different products sold by the candy machine
# 2. Let the customer make the selection
# 3. Show the customer the cost of the item selected
# 4. Accept money from the customer
# 5. Release the item

from CashRegisterimport CashRegister

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cashreg = CashRegister(200)
    print(cashreg.currentBalance)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
