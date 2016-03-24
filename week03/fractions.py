class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()


    def GCD(self, a, b):
    	if a % b == 0:
        	return b
    	else:
        	return self.GCD(b, a % b)

    def oprostqvane_na_angliiski(self):
    	x = self.GCD(self.numerator, self.denominator)
    	self.numerator //= x
    	self.denominator //= x

    	if self.numerator == self.denominator:
    		return 1

    	elif self.numerator == 0:
    		return 0

    	return Fraction(self.numerator, self.denominator)

    def __add__(self, other):
    	new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
    	new_denominator = self.denominator * other.denominator

    	new = Fraction(new_numerator, new_denominator)
    	return new.oprostqvane_na_angliiski()

    def __sub__(self, other):
    	new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
    	new_denominator = self.denominator * other.denominator

    	new = Fraction(new_numerator, new_denominator)
    	return new.oprostqvane_na_angliiski()

    def __mul__(self, other):
    	new_numerator = self.numerator * other.numerator
    	new_denominator = self.denominator * other.denominator

    	new = Fraction(new_numerator, new_denominator)
    	return new.oprostqvane_na_angliiski()

    def __eq__(self, other):
    	self.oprostqvane_na_angliiski()
    	other.oprostqvane_na_angliiski
    	return self.numerator == other.numerator and self.denominator == other.denominator

    def __hash__(self):
    	return hash(str(self.new_denominator) + "fjafgjaf")

def main():
	a = Fraction(1, 2)
	b = Fraction(2, 4)

	print(a == b)

	print(a + b)
	print(a - b)
	print(a * b)


if __name__ == "__main__":
	main()
