import sys
from random import randint


def main():
    filename = sys.argv[1]
    with open(filename, 'w') as data:
    	for i in range (0, int(sys.argv[2])):
    		data.write (str(randint(1, 1000)))
    		data.write (" ")

if __name__ == '__main__':
    main()