import sys


def main():
    for i in range(1, len(sys.argv)):
    	filename = sys.argv [i]
    	data = open(filename, 'r')
    	print(data.read())
    	data.close()

if __name__ == '__main__':
    main()