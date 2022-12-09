# Objective:
# The program should do the following:
# 1. Show the customer the different products sold by the candy machine
# 2. Let the customer make the selection
# 3. Show the customer the cost of the item selected
# 4. Accept money from the customer
# 5. Release the item

# from CashRegister import CashRegister
# from Dispenser import Dispenser
from CandyMachine import CandyMachine

# divided routine
def mainloop():
    # gathering orders from user till it exits
    # prints display menu
    candymach.showSelection()
    while True:
        try:
            usr_rawinput = input("Enter your choice: ")
            if usr_rawinput == "" or usr_rawinput == "\n":
                raise Exception
            usr_input = int(usr_rawinput)
            if ((usr_input > 4 and usr_input < 9) or (usr_input < 0 or usr_input > 9)):
                raise ValueError
            break
        except Exception as e:
            print("Bad choice here. Try again.", e)

    if (usr_input == 0):
        print("exiting...")
        exit()

    # for candy item
    if (usr_input == 1):
        cashchange = candymach.sellProduct(candymach.candy,candymach.cashreg)
        # if (not cashchange == 0 and cashchange is not None):
        #     print(f"You bought a candy. Your change is {cashchange}.\n")
    # for candy chips
    if (usr_input == 2):
        cashchange = candymach.sellProduct(candymach.chips,candymach.cashreg)
        # # if not (not cashchange == 0 and cashchange is not None):
        #     print(f"You bought a chips. Your change is {cashchange}.\n")
    # for gum item
    if (usr_input == 3):
        cashchange = candymach.sellProduct(candymach.gum,candymach.cashreg)
        # if not (not cashchange == 0 and cashchange is not None):
        #     print(f"You bought a gum. Your change is {cashchange}.\n")
    # for cooke item
    if (usr_input == 4):
        cashchange = candymach.sellProduct(candymach.cookies,candymach.cashreg)
        # if not (not cashchange == 0 and cashchange is not None):
        #     print(f"You bought a cookie. Your change is {cashchange}.\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    candymach = CandyMachine()
    while True:
        mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
