from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return (
            type(self) == type(other) and
            self._amount == other._amount
        )

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency

class Dollar(Money):

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)

class Franc(Money):

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = "CHF"

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)
