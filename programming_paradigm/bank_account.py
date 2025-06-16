class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available."""
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")