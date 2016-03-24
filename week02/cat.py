import sys


def main():
	filename = sys.argv[1]
	with open(filename, 'r') as data:

		print(data.read())

if __name__ == '__main__':
	main()