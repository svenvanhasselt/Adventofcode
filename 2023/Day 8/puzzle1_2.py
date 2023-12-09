import re
import math

def parse_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    map = []
    for index, line in enumerate(lines):
        new_line = line.replace("\n", "")
        if index == 0:
            instruct = new_line
        else:
            map.append(re.findall_list(r'\b\w+\b', line)) if line[0].isalnum() else None
    replace_num(map)
    return instruct, map

def search_loc(map, loc):
    for int, line in enumerate(map):
        if line[0] == loc:
            return int

def replace_num(map):
    for line in map:
        line[1] = search_loc(map, line[1])
        line[2] = search_loc(map, line[2])

def find_start(map):
    start_p = []
    for index, m in enumerate(map):
        if m[0][2] == 'A':
            start_p.append(index)
    return start_p

def part1_solution(instruct, map):
    index = next((index for index, m in enumerate(map) if m[0] == 'AAA'), None)
    match = map[index]
    
    i = 0
    count = 0
    while True:
        if instruct[i] == 'L':
            match = map[int(match[1])]
        else:
            match = map[int(match[2])]
        count += 1
        if match[0] == 'ZZZ':
            break
        i = (i + 1) % len(instruct)
    print('Part 1:', count)

def part2_solution(instruct, map):
    start_point =  find_start(map)
    check = [0] * len(start_point)

    for j, start in enumerate(start_point):
        next = map[start]
        i = 0
        while True:
            if instruct[i] == 'L':
                next = map[int(next[1])]
            else:
                next = map[int(next[2])]
            check[j] += 1
            if next[0][2] == 'Z':
                break
            i = (i + 1) % len(instruct)
    print('Part 2:', math.lcm(*check))

def main():
    instruct, map = parse_input('../Input/day8_1')
    
    part1_solution(instruct, map)
    part2_solution(instruct, map)

if __name__ == "__main__":
    main()
