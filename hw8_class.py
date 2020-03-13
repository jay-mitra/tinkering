class OverdraftException(Exception):
    pass

class BankAccount():

    def __init__(self, initial_balance):
        """ initalise the BankAccount object and track the initial balance """
        self.statement = []
        self.statement.append(initial_balance)
        self.balance = initial_balance

    def transaction(self, amount):
        """ generic method used for both deposits and withdrawals, by passing positive or negative amounts """
        self.statement.append(amount)
        if abs(amount) > self.balance:
            raise OverdraftException
        else:
            self.balance = self.balance + amount
