# Account class
class Account:
    def __init__(self, init_balance: float):
        self._balance = init_balance

    def getBalance(self) -> float:
        return self._balance

    def deposit(self, amt: float) -> bool:
        if amt > 0:
            self._balance += amt
            return True
        return False

    def withdraw(self, amt: float) -> bool:
        if 0 < amt <= self._balance:
            self._balance -= amt
            return True
        return False


# Customer class
class Customer:
    def __init__(self, f: str, l: str):
        self._firstName = f
        self._lastName = l
        self._account = None

    def getFirstName(self) -> str:
        return self._firstName

    def getLastName(self) -> str:
        return self._lastName

    def getAccount(self) -> Account:
        return self._account

    def setAccount(self, acct: Account):
        self._account = acct


# Bank class
class Bank:
    def __init__(self, bName: str):
        self._bankName = bName
        self._customers = []
        self._numberOfCustomers = 0

    def addCustomer(self, f: str, l: str):
        new_customer = Customer(f, l)
        self._customers.append(new_customer)
        self._numberOfCustomers += 1

    def getNumOfCustomers(self) -> int:
        return self._numberOfCustomers

    def getCustomer(self, index: int) -> Customer:
        if 0 <= index < len(self._customers):
            return self._customers[index]
        return None

bank = Bank("AI Bank")
bank.addCustomer("Sonic", "Hedgehog")
customer = bank.getCustomer(0)

account = Account(1000)
customer.setAccount(account)

customer.getAccount().deposit(200)
customer.getAccount().withdraw(150)

print(f"Customer: {customer.getFirstName()} {customer.getLastName()}")
print(f"Balance: {customer.getAccount().getBalance()}")
