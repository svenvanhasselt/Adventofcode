import re
from functools import cache

def parse_input(input):
    file = open(input, 'r')

    lines = file.readlines()

    arr = []
    groups = []
    for line in lines:
        line = line.replace('\n', '')
        line = re.sub(r'\.+', '.', line)
        split = line.split(' ')
        # arr.append(re.findall(r'[^.]+', split[0]))
        arr.append(split[0])
        num_list = [int(num) for num in split[1].split(',')]
        groups.append(num_list)
    
    return arr, groups

def is_valid(dots, blocks):
    count = 0
    found = []
    for c in dots:
        if c == '.':
            if count > 0:
                found.append(count)
            count = 0
        if c == '#':
            count += 1
    if count > 0:
        found.append(count)
    
    return tuple(found) == blocks    

all = {}
def find(dots, blocks, i):
    if i == len(dots):
        all[dots] = 1
        if is_valid(dots, blocks):
            return 1
        else:
            return 0
    if dots[i] == '?':
        return find(dots[:i] + '#' + dots[i + 1:], blocks, i+ 1) + find(dots[:i] + '.' + dots[i + 1:], blocks, i+ 1)
    else:
        return find(dots, blocks, i + 1)

def main():
    answer = 0
    dots, blocks = parse_input('input')
    blocks = [tuple(group) for group in blocks]
    mult = 0
    for i, d in enumerate(dots):
        d += mult * ('?' + d)
        blocks[i] += mult * blocks[i]
        answer += find(d, blocks[i], 0)
    print(answer)
if __name__ == "__main__":
    main()