import string

def five_kind(string_check):
    check_list = {char: 0 for char in 'AKQJT98765432'}
    for char in string_check:
        if char in check_list:
            check_list[char] += 1
    for char, count in check_list.items():
        if count == 5:
            return 7
    return 0

def four_kind(string_check):
    check_list = {char: 0 for char in 'AKQJT98765432'}
    for char in string_check:
        if char in check_list:
            check_list[char] += 1
    for char, count in check_list.items():
        if count == 4:
            return 6
    return 0

def three_kind_house(string_check):
    check_list = {char: 0 for char in 'AKQJT98765432'}
    for char in string_check:
        if char in check_list:
            check_list[char] += 1
    for char, count in check_list.items():
        if count == 3:
            for char1, count1 in check_list.items():
                if count1 == 2:
                    return 5
                elif count1 == 1:
                    return 4
    return 0

def two_pair(string_check):
    check_list = {char: 0 for char in 'AKQJT98765432'}
    for char in string_check:
        if char in check_list:
            check_list[char] += 1
    for char, count in check_list.items():
        if count == 2:
            check_list[char] = 0
            for char1, count1 in check_list.items():
                if count1 == 2:
                    return 3
    return 0

def one_pair(string_check):
    check_list = {char: 0 for char in 'AKQJT98765432'}
    for char in string_check:
        if char in check_list:
            check_list[char] += 1
    for char, count in check_list.items():
        if count == 2:
            return 2
    return 0

def check_score(string):
    score = five_kind(string)
    if score > 0:
        return score
    score = four_kind(string)
    if score > 0:
        return score
    score = three_kind_house(string)
    if score > 0:
        return score
    score = two_pair(string)
    if score > 0:
        return score
    score = one_pair(string)
    if score > 0:
        return score
    return 1

def main():
    file = open('../Input/day7_1', 'r')

    lines = file.readlines()

    full_list = []
    score = []
    for line in lines:
        line = line.replace('\n', '')
        split = line.split(" ")
        split.append(check_score(split[0]))
        full_list.append(split)
    order_seq = 'AKQJT98765432'
    full_list = sorted(full_list, key=lambda x: ([order_seq.index(char) for char in x[0]]), reverse=True)
    full_list = sorted(full_list, key=lambda x: x[2])

    sum = 0
    for rank, hand in enumerate(full_list):
        sum += int(hand[1]) * (rank + 1)
    print(sum)

if __name__ == "__main__":
    main()
