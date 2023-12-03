# Day 1 of Advent of Code 2023

import re

patterns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
file = open('input2', 'r')
Lines = file.readlines()

for line in Lines:
    match1 = re.search(r'\d', line)
    match2 = re.search(r'\d', line[::-1])
    found_patterns = None
    for char_i, char in enumerate(line):
        for pattern_index_i, pattern in enumerate(patterns):
            match_word = re.match(pattern, line[char_i:])
            if match_word:
                break
        if match_word:
                break
    for char_j, char in enumerate(line[::-1]):
        for pattern_index_j, pattern in enumerate(patterns):
            match_word2 = re.match(pattern, line[len(line) - char_j - 1:])
            if match_word2:
                break
        if match_word2:
                break
    if match1.start() > char_i:
        num1 = pattern_index_i + 1
    else:
        num1 = match1.group()
    if match2.start() < char_j:
        num2 = match2.group()
    elif not match_word2:
        num2 = match2.group()
    else:
        num2 = pattern_index_j + 1
    result = str(num1) + str(num2)
    sum += int(result)

print('sum:', sum)
file.close()