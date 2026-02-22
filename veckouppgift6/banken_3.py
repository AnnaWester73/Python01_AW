# Klass som representerar ett bankkonto


class Bankkonto:
    interest = 0.10                         # Gemensam ränta för alla bankkonton som skapas

    # Konstruktorn skapar ett nytt objekt för ett bankkonto med instansvariabel saldo.
    def __init__(self):
        self.saldo = 0                     # start saldo 0kr

    # Metod för att sätta in pengar
    def deposit(self, amount):
        if amount > 0:
            self.saldo = self.saldo + amount
        return self.saldo

    # Metod för att ta ut pengar
    def withdraw(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo = self.saldo - amount
            return True
        return False

    # Metod som lägger på ränta enligt klassens räntesats interest.
    def apply_interest(self):
        self.saldo = self.saldo + self.saldo * self.interest
        return self.saldo

    # Metod för att visa aktuellt saldo
    def balance(self):
        return self.saldo

   # Metod för att betala en räkning och returnerar saldo
   #  def pay_bill(self, amount):
   #      if 0 < amount <= self.saldo:
   #          self.saldo -= amount
   #      return self.saldo

    def pay_bill(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= amount
            return True
        else:
            return False
