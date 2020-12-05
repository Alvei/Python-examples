""" Context managers can be useful to rollback operations based on a condition (or exception).
    A context manager is a simple “protocol” (or interface) that your object needs to follow so
    it can be used with the with statement. Basically all you need to do is add __enter__ and __exit__
    methods to an object if you want it to function as a context manager.
    We need to add two dunder methods.
    https://www.python.org/dev/peps/pep-0343/
    https://dbader.org/blog/python-dunder-methods """


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
        print("\tENTER WITH: Making backup of transactions for rollback")
        self._copy_transaction = list(self._transaction)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Handle Exception if context manager is in place. Roll back the last transaction. """
        if self.balance < 0:
            self._transaction = self._copy_transaction
            print("ERROR: transaction cause negative balance, rollback!")


def validate_transaction(acc: Account, amount_to_add: float) -> none:
    """ Helper function that encapsulate the error checking. """
    with acc as a:
        a.add_amount(amount_to_add)
    print(f"Balance add {amount_to_add}: {acc.balance}")


def main():
    """ Test Harness"""
    acc = Account()
    print(f"Balance at beginning: {acc.balance}")

    validate_transaction(acc, 10)
    validate_transaction(acc, -20)


if __name__ == "__main__":
    main()

