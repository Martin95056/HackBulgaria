class BookReader:

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        return self

    def read_chapter(self):
        with open(self.filename, 'r') as f:
            start = f.read().find('#')
            stop = f.read()[start:].find('#')
            while True:
                if start == -1:
                    raise StopIteration
                chapter = f.read()[start:stop]
                start = stop
                stop = f.read()[start:].find('#')
                if stop == -1:
                    chapter = f.read()[start:]
                yield chapter

    def __next__(self):
        for chapter in self.read_chapter():
            user_input = input("Press n for next chapter: ")
            if user_input is 'n':
                return chapter


def main():
    a = BookReader('001.txt')

    for ch in a:
        print(ch)


if __name__ == '__main__':
    main()
