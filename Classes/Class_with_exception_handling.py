""" Context managers can be useful to rollback operations based on a condition (or exception). """

class Account:
    """ """
    def __init__(self) -> None:
        """ Initialize the class. Core data type is list. """
        self._transaction = []

    @property
    def balance(self) -> float:
        """ Sum all the transactions processed to create the balance. """
        return sum(self._transaction)

    def add_amount(self, amount: float) -> None:
        """ Add a new transaction. """
        self._transaction.append(amount)

    def __enter__(self):
        """ """
        self._copy_transaction = list(self._transaction)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Handle Exception if context manager is in place. Roll back the last transaction. """
        if self.balance < 0:
            self._transaction = self._copy_transaction
            print("ERROR: transaction cause negative balance, rollback!")

def main():
    """ Test Harness"""
    acc = Account()
    print(f"Balance: {acc.balance}")

    with acc as a:
        a.add_amount(10)
    print(f"Balance: {acc.balance}")

    a.add_amount(-20)
    print(f"Balance: {acc.balance}")

    with acc as a:
        a.add_amount(20)
    print(f"Balance: {acc.balance}")

    with acc as a:
        a.add_amount(-20)
    print(f"Balance: {acc.balance}")

if __name__ == "__main__":
    main()

