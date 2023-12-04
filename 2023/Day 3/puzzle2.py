# Day 3 of Advent of Code 2023
import re

def check_left(string, ast):
    ast -= 1
    number = ""
    while ast >= 0 and string[ast].isdigit():
        number += string[ast]
        ast -= 1
    if len(number) > 0:
        list = [(int(number[::-1]))]
        return list

def check_right(string, ast):
    ast += 1
    number = ""
    while ast < len(string) and string[ast].isdigit():
        number += string[ast]
        ast += 1
    if len(number) > 0:
        list = [(int(number))]
        return list

def find_start(string, index):
    temp_i = index
    while temp_i > 0 and string[temp_i].isdigit():
        temp_i -= 1
    temp_j = temp_i
    while temp_j < len(string) and ((temp_j < index + 2) or string[temp_j].isdigit()):
        temp_j += 1
    num_pattern = re.compile(r'\d+')
    match = num_pattern.finditer(string[temp_i:temp_j])
    for num in match:
        list.append(int(num.group()))
    if list:
        return list

def check_line(string, ast):
    ast -= 1
    index = ast
    while index < len(string) and (index - ast < 2 or string[index].isdigit()):
        if string[index].isdigit():
           find_start(string, index)
           break
        index += 1

file = open('../Input/day3_2', 'r')
Lines = file.readlines()

sum = 0
for index, line in enumerate(Lines):
    line = line.replace("\n", "")
    asterix_pat = re.compile(r'\*')
    match = asterix_pat.finditer(line)
    for m in match:
        list = []
        list.extend(check_left(line, m.start()) or [])
        list.extend(check_right(line, m.start()) or [])
        list.extend(check_line(Lines[index - 1], m.start() if index != 0 else None) or [])
        list.extend(check_line(Lines[index + 1], m.start() if index < len(Lines) - 1 else None) or [])
        if len(list) == 2:
           sum += list[0] * list[1]
print(sum)
file.close()