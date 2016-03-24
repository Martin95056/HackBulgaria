import collections


class Bill:

    def __init__(self, amount):
        if amount < 0:
            raise ValueError
        if type(amount) is not int:
            raise TypeError
        self._amount = amount

    def __str__(self):
        return "A {}$ bill".format(self._amount)

    def __repr__(self):
        return "{}".format(self._amount)

    def __int__(self):
        return int(self._amount)

    def __eq__(self, other):
        return self._amount == other._amount

    def __lt__(self, other):
        return self._amount < other._amount

    def __hash__(self):
        return hash(str(self._amount) + "adajdajda")


class BatchBill:

    def __init__(self, bill):
        self._bill = bill

    def __len__(self):
        return int(len(self._bill))

    def total(self):
        s = 0
        for i in self._bill:
            s += int(i)
        return s

    def __getitem__(self, index):
        return self._bill[index]


class CashDesk:

    def __init__(self):
        self._cash = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self._cash.append(money)

        elif isinstance(money, BatchBill):
            self._cash.extend(money)

        return self._cash

    def total(self):
        suma = 0
        for i in range(0, len(self._cash)):
            suma += int(self._cash.__getitem__(i))

        return suma

    def inspect(self):
        dic = {}
        first_str = "We have a total of {}$ in the desk\n".format(self.total())
        second_str = "We have the following count of bills, sorted in ascending order:\n"
        for i in self._cash:
            dic[int(i)] = self._cash.count(i)
        third_str = ""
        od = collections.OrderedDict(sorted(dic.items()))
        for k, v in od.items():
            third_str += "{}$ bills - {}\n".format(k, v)

        return first_str + second_str + third_str[:-1]


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total())
print(desk.inspect())
