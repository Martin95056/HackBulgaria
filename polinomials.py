import sys


class Monom:
    def __init__(self, coeff, variable, power):
        self._coeff = coeff
        self._variable = variable
        self._power = power

    def power_0(self):
        return self._power == 0

    def power_1(self):
        return self._power == 1

    def __str__(self):
        if self.power_0:
            return '{}'.format(self._coeff)

        elif self.power_1:
            return '{}{}'.format(self._coeff, self._variable)

        else:
            return '{}{}^{}'.format(self._coeff, self._variable, self._power)

    def __repr__(self):
        return self.__str__

    def __add__(self, other):
        if self.eq_power(other):
            return Monom(int(self._coeff) + int(other._coeff),
                         self._variable,
                         self._power)

    def eq_power(self, other):
        return self._variable == other._variable\
                    and self._power == other._power

    def derive(self):
        if self.power_0():
            return 0

        elif self.power_1():
            return self._coeff

        else:
            return Monom(int(self._coeff) * int(self._power),
                         self._variable,
                         int(self._power) - 1)


class Polynom:
    def __init__(self, polynom):
        self.polynom = polynom

    def __str__(self):
        return '+'.join(self.polynom)

    def __repr__(self):
        return self.polynom.__str__

    def bubble_sort(self):
        for passnum in range(len(self.polynom) - 1, 0, -1):
            for i in range(passnum):
                if self.polynom[i]._power < self.polynom[i + 1]._power:
                    temp = self.polynom[i]
                    self.polynom[i] = self.polynom[i + 1]
                    self.polynom[i + 1] = temp

    def output(self):
        print("The derivative of f(x) = {} is: ".format("+".join(self.polynom)))

    def add_eq_powers(self):
        pass

    def add_derivatives(self):
        der_list = []
        for monom in self.polynom:
            der_list.append(monom.derive())

        return "+".join(der_list)


class Derivative:
    def __init__(self):
        self._polynomial = sys.argv[1].split("+")

    def bubble_sort(self):
        for i in range(len(self._polynomial) - 1, 0, -1):
            if self._polynomial[i][-1] < self._polynomial[i + 1][-1]:
                temp = self._polynomial[i]
                self._polynomial[i] = self._polynomial[i + 1]
                self._polynomial[i + 1] = temp

    def output(self):
        return "The derivative of f(x) = {} is :".format(sys.argv[1])

    def derivative(self):
        result = []
        for element in self._polynomial:
            if int(element) is True:
                result.append('0')

            elif '^' not in element:
                result.append(element[0: len(element) - 1])
            else:
                result.append('{}x^{}'.format(int(element[0: element.find('x')]) * int(element[element.find('^') + 1:]),
                                              int(element[element.find('^') + 1:]) - 1))

        return self.output() + '\nf\'(x) = ' + '+'.join(result)


def main():
    polynom = Polynom(sys.argv[1].split('+'))

    polynom.output()
    polynom.add_derivatives()

if __name__ == '__main__':
    main()
