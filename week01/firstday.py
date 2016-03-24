import math


def sum_of_digits(n):
    sum = 0
    if n < 0:
        n = math.sqrt(n ** 2)
    while n:
            sum += n % 10
            n //= 10
    return sum


def to_digits(n):
    return [int(i) for i in str(n)]

def to_number(digits):
    new = ""
    for i in digits:
        new += str(i)
    return int(new)


def fact_number(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def fact_digits(number):
    s = 0
    for i in to_digits(number):
        s += fact_number(i)
    return s


def fibonacci(n):
    fib_list = []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    a, b = 1, 1
    fib_list.append(a)
    fib_list.append(b)
    while n > len(fib_list):
            next = a + b
            a = b
            b = next
            fib_list.append(next)
    return fib_list


def fib_number(n):
    return to_number(fibonacci(n))

def palindrome(obj):
    return str(obj) == str(obj)[::-1]

def count_vowels(str):
    sum_vowels = 0
    vowels = "aeouiy"
    for i in str.lower():
        for vowel in vowels:
            if i == vowel:
                sum_vowels += 1
    return sum_vowels

def count_consonants(str):
    sum_cons = 0
    cons = "bcdfghjklmnpqrstvwxz"
    for i in str.lower():
        for con in cons:
            if i == con:
                sum_cons += 1
    return sum_cons            

def char_histogram(string):
    dictionary = { }
    repeat = 1
    for i in string:
        if string.count(i) > 1:
            repeat = string.count(i)
        dictionary[i] = repeat
    return dictionary
