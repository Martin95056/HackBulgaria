import sys
from itertools import *

def main():
	suma = 0
	number = '0'
	res = []
	with open ('number.txt', 'r') as data:
		string = data.read()
		for i in string:
			if i.isdigit():
				number += i

			else:
				res.append (number)
				number = '0'

		res.append (number)

		for x in res:
			suma += int(x)

	print(suma)


if __name__ == '__main__':
	main()