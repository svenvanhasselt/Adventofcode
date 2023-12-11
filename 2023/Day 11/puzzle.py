import math
import numpy as np
from itertools import combinations

def parse_input(input):
    file = open(input, 'r')

    lines = file.readlines()

    map = []
    for line in lines:
        line = line.replace('\n', '')
        map.append(list(line))
    
    map = np.array(map)

    return map

def check_y(map, x):
    for row in map:
        if row[x] == '.':
            continue
        else:
            return False
    return True

def check_x(string):
    for c in string:
        if c == '.':
            continue
        else:
            return False
    return True

def check_expand(map):
    exp_x = []
    exp_y = []
    for x, col in enumerate(map[0]):
        if check_y(map, x):
            exp_x.append(x)
    for y, row in enumerate(map):
        if check_x(row):
            exp_y.append(y)
    return exp_x, exp_y

def find_galaxies(map):
    coordinates = []
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == '#':
                coordinates.append((y, x )) 
        
    return coordinates

def expand_coordinates(map, coordinates, exp):
    exp_x, exp_y = check_expand(map)

    for i, c in enumerate(coordinates):
        count = 0
        for ex in exp_x:
            if c[1] >= ex:
                count += 1
            coordinates[i] = c[0], c[1] + (count * exp)
    for i, c in enumerate(coordinates):
        count = 0
        for ex in exp_y:
            if c[0] >= ex:
                count += 1
            coordinates[i] = c[0] + (count * exp), c[1]
    return coordinates

def calculate_shortest_paths(map, exp):
    coordinates = find_galaxies(map)
    coordinates = expand_coordinates(map, coordinates, exp)

    sum = 0
    com = combinations(coordinates, 2)
    for pair in com:
        A, B = pair
        dist = abs(B[1] - A[1]) + abs(B[0] - A[0])
        sum += dist
    return (sum)

def main():
    map = parse_input('../Input/day11')
    print('Part 1:', calculate_shortest_paths(map, 1))
    print('Part 2:', calculate_shortest_paths(map, 999999))

if __name__ == "__main__":
    main()