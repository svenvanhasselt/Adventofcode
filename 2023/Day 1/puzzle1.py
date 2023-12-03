# Day 1 of Advent of Code 2023
import re

sum = 0
file = open('test', 'r')
Lines = file.readlines()

for line in Lines:
    match1 = re.search(r'\d', line)
    if match1:
        print('Num is:', match1.group())
    match2 = re.search(r'\d', line[::-1])
    result = match1.group() + match2.group()
    sum += int(result)

print('sum:', sum)
file.close()