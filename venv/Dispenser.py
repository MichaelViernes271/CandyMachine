class Dispenser:
    """releases selected items, if not empty. shows costs and remaining items"""

    def __init__(self, numberOfItems=50, cost=50):
        """assigns def item size and cost"""

        if numberOfItems <= 0 or cost <= 0:
            numberOfItems = 50
            cost = 50
        else:
            self.numberOfItems = numberOfItems
            self.cost = cost

    def getCount(self):
        """gets count of items"""
        return self.numberOfItems

    def getProductCost(self):
        """gets item cost"""
        return self.cost

    def makeSale(self):
        """decrements item size by 1"""
        self.numberOfItems -= 1

if __name__ == "__main__": # for testing class dispenser
    d1 = Dispenser()
    d2 = Dispenser()  # expects def value

    print(d1.getProductCost())
    print(d1.getCount())
    print(d1.makeSale())
    print(d1.getCount())
    print("=" * 10)
    print(d2.makeSale())
    print(d2.getProductCost())
    print(d2.getCount())
