import math


# Question 1, 2
class Fraction:
    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__reduced = False

    @property
    def numerator(self):
        self.reduce()
        return self.__numerator

    @property
    def denominator(self):
        self.reduce()
        return self.__denominator

# Question 3

    def reduce(self):
        if self.__reduced == True:
            return None
        gcd = math.gcd(abs(int(self.__numerator)),
                       abs(int(self.__denominator)))
        if self.__denominator * self.__numerator < 0:
            if self.__denominator < 0:
                self.__denominator = (-self.__denominator // gcd)
                self.__numerator = -(self.__numerator // gcd)
            elif self.__denominator > 0:
                self.__denominator = self.__denominator // gcd
                self.__numerator = self.__numerator // gcd
        if self.__denominator * self.__numerator > 0:
            if self.__denominator > 0:
                self.__denominator = self.__denominator // gcd
                self.__numerator = self.__numerator // gcd
            elif self.__denominator < 0:
                self.__denominator = -(self.__denominator // gcd)
                self.__numerator = -(self.__numerator // gcd)
        self.__reduced = True

# Question 5

    def __repr__(self):
        return f'Fraction({self.__numerator}, {self.__denominator})'

    def __str__(self):
        self.reduce()
        return f'{self.__numerator}/{self.__denominator}'

# Question 6

    def __eq__(self, other):
        if self.__denominator * other.__numerator == self.numerator * other.__denominator:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__denominator * other.__numerator == self.numerator * other.__denominator:
            return False
        else:
            return True


# Question 7

    def __add__(self, other):
        a = self.__denominator * other.__numerator + self.numerator * other.__denominator
        b = self.__denominator * other.__denominator
        return Fraction(a, b)

    def __sub__(self, other):
        a = self.__denominator * other.__numerator - self.numerator * other.__denominator
        b = self.__denominator * other.__denominator
        return Fraction(a, b)

    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)

    def __mul__(self, other):
        a = self.__numerator * other.__numerator
        b = self.__denominator * other.__denominator
        return Fraction(a, b)

    def __truediv__(self, other):
        a = self.__numerator * other.__denominator
        b = self.__denominator * other.__numerator
        return Fraction(a, b)