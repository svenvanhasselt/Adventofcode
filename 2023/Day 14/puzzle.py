from functools import cache
import sys
import re

def parse_input(input):
    file = open(input, 'r')

    lines = file.readlines()
    platform = tuple(line.rstrip() for line in lines)
    return platform 

def change_tuple(platform, i, j, char):
    platform =  [list(row) for row in platform]
    platform[j][i] = char
    platform = tuple(tuple(row) for row in platform)
    return platform

def calculate_result(platform):
    length = len(platform)
    sum = 0
    for i, line in enumerate(platform):
        sum += line.count('O') * (length - i)
    return sum

def search_last(platform, i, j):
    while j < len(platform):
        if j == 0 and platform[j][i] == '.':
            return j
        if j + 1 < len(platform) and platform[j][i] == 'O' and platform[j + 1][i] == '.':
            last = j + 1
            return (last)
        if j + 1 < len(platform) and platform[j][i] == '#' and platform[j + 1][i] == '.':
            last = j + 1
            return (last)
        j += 1
    return j - 1

def tilt_north(platform):
    i = 0
    while i < len(platform[0]):
        last = search_last(platform, i, 0)
        j = 0
        while j < len(platform):
            if platform[j][i] == 'O' and j > last:
                platform = change_tuple(platform, i, last, 'O')
                platform = change_tuple(platform, i, j, '.')
                last = search_last(platform, i, last)
            if platform[j][i] == '#':
                last = search_last(platform, i, j)
            j += 1
        i += 1
    return platform


def rotate_tuple(platform):
    rows, cols = len(platform), len(platform[0])
    platform = tuple(
            platform[row][col]
            for col in range(cols)
            for row in range(rows - 1, -1, -1)
        )
    return tuple(platform[i:i + rows] for i in range(0, len(platform), rows))

@cache
def tilt_rotate(platform):
    i = 0
    while i < 4:
        platform = tilt_north(platform)
        platform = rotate_tuple(platform)
        i += 1
    return platform

@cache
def find_cycle(platform, cycles):
    cycle = 0
    seen = {}
    while cycle < cycles:
        platform = tilt_rotate(platform)
        if platform in seen:
            return rotate_cycle(platform, (cycles - cycle - 1) % (cycle - seen[platform] ))         
        seen[platform] = cycle
        cycle += 1

@cache
def rotate_cycle(platform, cycles):
    cycle = 0
    while cycle < cycles:
        platform = tilt_rotate(platform)
        cycle += 1
    return platform

def main():
    platform = parse_input('input')
    print('Part 1:', calculate_result(platform = tilt_north(platform)))
    platform = find_cycle(platform, 1000000000)
    print('Part 2:', calculate_result(platform))

if __name__ == "__main__":
    main()