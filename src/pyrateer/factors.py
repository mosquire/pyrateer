from abc import ABC, abstractmethod


class RatingFactor(ABC):
    def __init__(self, name, lookup):
        self.name = name
        self.lookup = lookup

    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        return CompoundFactor(self, other, operator="+")

    def __sub__(self, other):
        return CompoundFactor(self, other, operator="-")

    def __mul__(self, other):
        return CompoundFactor(self, other, operator="*")


class NumericFactor(RatingFactor):
    def calculate(self, input):
        if input in self.lookup:
            return self.lookup[input]
        elif input < min(self.lookup.keys()):
            return self.lookup[min(self.lookup.keys())]
        elif input > max(self.lookup.keys()):
            return self.lookup[max(self.lookup.keys())]
        else:
            return linterp(input, self.lookup)


class CategoricalFactor(RatingFactor):
    def calculate(self, input):
        return self.lookup[input]


class ConstantFactor(RatingFactor):
    def calculate(self, input=None):
        if input is not None:
            raise ValueError("Constant factor should not have an input")
        return self.lookup


class CompoundFactor(RatingFactor):
    def __init__(self, lhs, rhs, operator):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator

    def calculate(self, **rate_params):
        if isinstance(self.lhs, CompoundFactor):
            lhs_value = self.lhs.calculate(**rate_params)
        else:
            lhs_value = self.lhs.calculate(rate_params.get(self.lhs.name))
        if isinstance(self.rhs, CompoundFactor):
            rhs_value = self.rhs.calculate(**rate_params)
        else:
            rhs_value = self.rhs.calculate(rate_params.get(self.rhs.name))
        if self.operator == "+":
            return lhs_value + rhs_value
        elif self.operator == "-":
            return lhs_value - rhs_value
        elif self.operator == "*":
            return lhs_value * rhs_value
        else:
            raise NotImplementedError(f"Operator {self.operator} not implemented")


def linterp(input, lookup):
    keys = sorted(lookup.keys())
    for i in range(len(keys) - 1):
        if keys[i] <= input < keys[i + 1]:
            pct_traveled = (input - keys[i]) / (keys[i + 1] - keys[i])
            return lookup[keys[i]] + pct_traveled * (
                lookup[keys[i + 1]] - lookup[keys[i]]
            )
