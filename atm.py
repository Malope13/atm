from decimal import Decimal, InvalidOperation
from getpass import getpass


ATM_PIN = "1234"
MAX_PIN_ATTEMPTS = 3


def read_amount(prompt):
    """Read a positive amount with at most two decimal places."""
    try:
        amount = Decimal(input(prompt).strip())
    except InvalidOperation:
        print("Please enter a valid amount.")
        return None

    if not amount.is_finite() or amount <= 0 or amount.as_tuple().exponent < -2:
        print("Enter an amount greater than zero with no more than two decimal places.")
        return None
    return amount.quantize(Decimal("0.01"))


def main():
    balance = Decimal("1000.00")

    print("=== Welcome to the ATM ===")
    for _ in range(MAX_PIN_ATTEMPTS):
        if getpass("Enter your PIN: ") == ATM_PIN:
            break
        print("Incorrect PIN.")
    else:
        print("Too many incorrect attempts. Access denied.")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check balance")
        print("2. Deposit cash")
        print("3. Withdraw cash")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            print(f"Your balance is ${balance:.2f}")
        elif choice == "2":
            amount = read_amount("Amount to deposit: $")
            if amount is not None:
                balance += amount
                print(f"Deposit successful. New balance: ${balance:.2f}")
        elif choice == "3":
            amount = read_amount("Amount to withdraw: $")
            if amount is not None:
                if amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful. New balance: ${balance:.2f}")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
