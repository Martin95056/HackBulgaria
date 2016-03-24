import copy


def to_digits(n):
    list = []
    for i in str(n):
        list.append(int(i))

    return list


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def to_number(digits):
    new = " "
    for i in digits:
        new += str(i)
    return int(new)


def is_number_balanced(n):
    a = to_digits(n)
    sum_i = 0
    sum_j = 0
    middle_len = len(a) // 2

    if len(a) % 2 == 0:
        for i in range(0, middle_len):
            sum_i += a[i]
        for j in range(middle_len, len(a)):
            sum_j += a[j]
    else:
        for i in range(0, middle_len):
            sum_i += a[i]
        for j in range(middle_len + 1, len(a)):
            sum_j += a[j]

    return sum_i == sum_j


def is_increasing(seq):
    if len(seq) == 1:
        return seq
    else:
        for i in range(0, len(seq) - 1):
            return seq[i] < seq[i + 1] and seq[len(seq) - 1] > seq[len(seq) - 2]


def is_decreasing(seq):
    for i in range(0, len(seq) - 1):
        return seq[i] > seq[i + 1] and seq[len(seq) - 1] < seq[len(seq) - 2]


def reverse(num):
    return int(str(num)[::-1])


def make_palindrome(n):
    get_pal = to_digits(n)
    middle_len = len(get_pal) // 2
    list = []

    if len(get_pal) % 2 == 1:
        for i in range(0, middle_len):
            list.append(get_pal[i])
        pal = reverse(to_number(list))
        list.append(get_pal[middle_len])
        list.append(pal)
    else:
        for i in range(0, middle_len):
            list.append(get_pal[i])
        pal = reverse(to_number(list))
        list.append(pal)
    return to_number(list)


def get_largest_palindrome(n):
    if palindrome(n):
        new = to_digits(n)
        if len(new) % 2 == 1:
            new[len(new) // 2] -= 1
        else:
            new[0] -= 1
            new[len(new) - 1] -= 1
        return to_number(new)
    else:
        return make_palindrome(int(n))


def prime_numbers(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n+1)//2-1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2*i+3
    return [2]+[x for x in s if x]


def is_anagram(a, b):
    if len(a) != len(b):
        return False

    newA = a.lower()
    newB = b.lower()
    for x in newA:
        if x not in newB:
            return False
    return True


def birthday_ranges(birthdays, ranges):
    sum_people = 0
    list_births = []
    for dates in range(0, len(ranges)):
        for date_of_birth in birthdays:
            if date_of_birth in range(ranges[dates][0], ranges[dates][1] + 1):
                sum_people += 1
        list_births.append(sum_people)
        sum_people = 0

    return list_births


def is_transversal(transversal, family):
    for group in family:
        it = [x for x in group if x in transversal]
        if len(it) == 0 or len(it) > 1:
            return False

    return True


NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def sum_matrix(matrix):
    return sum([sum(row) for row in matrix])


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result
