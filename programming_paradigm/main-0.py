import sys
from bank_account import BankAccount

def main():
    # Initialize account with a starting balance of 100
    account = BankAccount(100)
    
    # Check if a command was provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount
    command, *params = sys.argv[1].split(':')
    
    try:
        # Convert amount to float if provided
        amount = float(params[0]) if params else None
        
        if command == "deposit" and amount is not None:
            if account.deposit(amount):
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Invalid deposit amount.")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds or invalid amount.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")
    except (ValueError, IndexError):
        print("Invalid input format. Use <command>:<amount> or <command> for display.")

if __name__ == "__main__":
    main()