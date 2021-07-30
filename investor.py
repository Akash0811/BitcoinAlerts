class Investor:
    def __init__(initial,bit_initial=0):
        self.cash= initial
        self.bitcoin = bit_initial

    def allin(price):
        self.bitcoin += self.cash/price
        self.cash = 0

    def allout(price):
        self.cash += price*self.bitcoin
        self.bitcoin = 0

    def buy(amt,price):
        if self.cash/bitcoin > amt:
            print("Insufficient funds")
        else:
            self.bitcoin += amt
            self.cash -= amt*price

    def sell(amt,price):
        if self.bitcoin < amt:
            print("Insufficient funds")
        else:
            self.bitcoin -= amt
            self.cash += amt*price
