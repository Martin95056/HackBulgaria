def chain(i1, i2):
    for i in i1:
        yield i
    for i in i2:
        yield i


def compress(iterable, mask):
    for i in range(len(iterable)):
        if mask[i] is True:
            yield iterable[i]


def cycle(iterable):
    while True:
        for i in list(chain(iterable, iterable)):
            yield i
