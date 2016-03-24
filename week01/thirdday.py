from itertools import *

def count_words(arr):
    dic = {}
    for i in arr:
        dic[i] = arr.count(i)

    return dic

def nan_expand(times):
    if times == 0:
        return ""

    s = "NaN"
    for i in range(1, times + 1):
        s = "Not a " + s

    return s

def iterations_of_nan_expand(expanded):
    repeat = 0
    a = expanded.count("Not a ")
    if a > 0:
        repeat += a

    elif expanded == "":
        repeat = 0

    else:
        return False

    return repeat

def group(arr):
    return [list(g) for k, g in groupby(arr)]

def max_consecutive(items):
    grouped_items = group(items)
    max_len = len(grouped_items[0])
    for i in grouped_items:
        if len(i) > max_len:
            max_len = len(i)

    return max_len

def gas_stations(distance, tank_size, stations):
    stops = []
    stations.insert(0, 0)

    for i in range(1, len(stations) -1):
        
        if stations[i + 1] - stations[i - 1] >= tank_size:
            stops.append (stations[i])
            tank_size = tank_size

    if distance - stations[len(stations) - 2] >= tank_size:
        stops.append (stations[len(stations) - 1])

    return stops

def sum_of_numbers(st):
    s = 0
    number = '0'
    result = []
    for i in st:
        if i.isdigit():
            number += i

        else:
            result.append (number)
            number = '0'
            
    result.append (number)

    for x in result:
        s += int(x)

    return s

NUMBERS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ' ',
    -1: ''
}

def numbers_to_message(num):
    res = ""
    numbs_groups = group(num)
    up_c = False

    for grp in numbs_groups:
        if grp[0] == 1:
            up_c = True
            continue
        if grp[0] == -1:
            continue

        key_letters = NUMBERS[grp[0]]
        times_pressed = len(grp)
        selected_letter_index = times_pressed % len(key_letters) - 1
        letter = key_letters[selected_letter_index]

        if up_c:
            res += letter.upper()
            up_c = False

        else:
            res += letter

    return res

def message_to_numbers(message):
    result = []
    for k in NUMBERS.keys():
        for l in range(len(message) - 1):
            if message[l].isupper():
                result.append(1)
            lower_letter = message[l].lower()
            multiplyer = NUMBERS[k].find(lower_letter) + 1
            for i in range(multiplyer):
                result.append(k)
            if message[l + 1].lower() in NUMBERS[k]:
                result.append(-1)

        m = NUMBERS[k].find(message[len(message) - 1]) + 1
        for i in range(m):
            result.append(k)

    return result

print(message_to_numbers("Ivo e Panda"))
