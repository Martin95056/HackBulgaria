import sys
import os.path


def main():
	path = sys.argv [1]
	print(str(path), "size is", 1.0 * 10 ** -9 * os.path.getsize (path), "GB")
	

if __name__ == '__main__':
	main()