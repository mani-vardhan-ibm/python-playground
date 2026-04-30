# Object-Oriented Programming in Python
# ----------------------------------------

class Animal:
    """Base class for all animals."""

    species_count = 0  # class variable

    def __init__(self, name, sound):
        self.name = name        # instance variable
        self.sound = sound
        Animal.species_count += 1

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"

    def __repr__(self):
        return f"Animal(name={self.name!r}, sound={self.sound!r})"


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def __init__(self, name, breed):
        super().__init__(name, sound="Woof")
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def speak(self):
        # Override parent method
        return f"{self.name} barks: {self.sound}! {self.sound}!"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def __init__(self, name, indoor=True):
        super().__init__(name, sound="Meow")
        self.indoor = indoor


# Usage
dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
print(dog.fetch("ball"))
print(f"Total animals: {Animal.species_count}")

# isinstance and issubclass
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True

# Dunder methods
print(str(dog))   # Animal(Rex)
print(repr(dog))  # Animal(name='Rex', sound='Woof')


# Encapsulation with properties
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance  # "protected" by convention

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"BankAccount({self.owner}, balance=${self._balance:.2f})"


account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account)  # BankAccount(Alice, balance=$1300.00)
