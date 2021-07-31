class Investor:
    def __init__(self,initial,bit_initial=0):
        self.cash= initial
        self.bitcoin = bit_initial

    def allin(self,price):
        self.bitcoin += self.cash/price
        self.cash = 0

    def allout(self,price):
        self.cash += price*self.bitcoin
        self.bitcoin = 0

    def buy(self,amt,price):
        if self.cash/bitcoin > amt:
            print("Insufficient funds")
        else:
            self.bitcoin += amt
            self.cash -= amt*price

    def sell(self,amt,price):
        if self.bitcoin < amt:
            print("Insufficient funds")
        else:
            self.bitcoin -= amt
            self.cash += amt*price

    def total_worth(self,price):
        return self.cash+self.bitcoin*price
