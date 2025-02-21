from accounts.account import Account
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException


class MortgageAccount(Account):

    def __init__(self, firstname, lastname, loan_amount, loan_term):
        super().__init__(firstname, lastname, loan_amount, loan_term)
        # self._minimum_balance = minimum_balance
        self._loan_amount = loan_amount
        self._loan_term = loan_term
    def withdraw(self, amount):
        if amount >= 0 and self._balance - amount > self._minimum_balance:
            self._balance -= amount
        else:
            breach_amount = self._minimum_balance - (self._balance - amount)
            raise MinimumBalanceBreachedException(breach_amount)


