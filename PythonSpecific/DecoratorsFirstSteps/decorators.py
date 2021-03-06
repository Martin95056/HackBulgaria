from datetime import datetime
import time


def accepts(*args1):
    def decorator(func):
        def decorated(*args2):
            for i in args2:
                if type(i) not in args1:
                    raise TypeError("Argument {} of {} is not in {}".
                                    format(i,
                                           func.__name__,
                                           args1.__name__))
            return func(*args2)
        return decorated
    return decorator


def encrypt(key):
    def acceptor(func):
        def decorated():
            result = func().split(' ')
            new_word = ""
            new_res = []
            for word in result:
                for i in word:
                    i = chr(ord(i) + key)
                    new_word += i
                new_res.append(new_word)
                new_word = ""
            return ' '.join(new_res)
        return decorated
    return acceptor


def log(filename):
    def acceptor(func):
        def decorated(*args, **kwargs):
            with open(filename, 'a') as f:
                f.write("{} called at {}\n".
                        format(func.__name__, datetime.now()))
                return func(*args, **kwargs)
        return decorated
    return acceptor


def performance(filename):
    def acceptor(func):
        def decorated(*args, **kwargs):
            start_time = time.time()
            with open(filename, 'a') as f:
                f.write("{} called and tooked {}\n".
                        format(func.__name__, time.time() - start_time))
                return func(*args, **kwargs)
        return decorated
    return acceptor

