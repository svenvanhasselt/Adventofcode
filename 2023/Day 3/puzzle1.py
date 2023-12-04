# Day 3 of Advent of Code 2023
import re

def check_symbols(string):
    alpha_num_pattern = re.compile(r'[^a-zA-Z0-9.]')
    return bool(alpha_num_pattern.search(string))

sum = 0
string = ""
file = open('../Input/day3_1', 'r')
Lines = file.readlines()
for index, line in enumerate(Lines):
    line = line.replace("\n", "")
    pattern = re.compile(r'\d+')
    matches = pattern.finditer(line)
    for match in matches:
        start = max(0, match.start() - 1)
        end = min(match.end() + 1, len(line))
        if index != 0:
            string += (Lines[index - 1][start:end])
        if index != len(Lines) - 1:
            string += (Lines[index + 1][start:end])
        string += line[start]
        string += line[end - 1]
        if check_symbols(string) is True:
            sum += int(line[match.start():match.end()])
        string = ""
print(sum)
file.close()