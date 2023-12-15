import re

def parse_input(input):
    file = open(input, 'r')

    lines = file.readlines()

    blocks = []
    block = []
    for line in lines:
        line = line.replace('\n', '')
        if line == '':
            blocks.append(block)
            block = []
        else:
            block.append(line)
    blocks.append(block)
    
    return (blocks)

def check_line_v(block, j):
    for i, line in enumerate(block):
        check1 = False
        check2 = False
        if line[:j][::-1].startswith(line[j:]):
            check1 = True
        if j != 0 and line[j:].startswith(line[:j][::-1]):
            check2 = True
        if check1 == True or check2 == True:
            continue
        else:
            return False
    return True

def check_line_h(block, i):
    for j, char in enumerate(block[i]):
        first =  ''.join(row[j] for row in block[:i])
        second = ''.join(row[j] for row in block[i:])
        check1 = False
        check2 = False
        if first[::-1].startswith(second):
            check1 = True
        if i != 0 and second.startswith(first[::-1]):
            check2 = True
        if check1 == True or check2 == True:
            continue
        else:
            return False
    return True

def change_char(block, i, j, char):
    if 0 <= i < len(block) and 0 <= j < len(block[i]):
        block[i] = list(block[i])
        block[i][j] = char
        block[i] = ''.join(block[i])
    return block

def find_line_smudge(block, v_r, h_r):
    for i, line in enumerate(block):
        if check_line_h(block, i) and i != h_r:
            return i * 100


    for j, c in enumerate(block[0]):
        if check_line_v(block, j) and j != v_r:
            return j
   
def find_prev(block, ):
    hor_res = None
    vert_res = None
    for x, char in enumerate(block[0]):
        if check_line_v(block, x):
            vert_res = x
    for y, line_p in enumerate(block):
        if check_line_h(block, y) == True:
            hor_res = y
    return vert_res, hor_res

def find_line(blocks):
    part1 = 0
    part2 = 0
    hor_res = None
    vert_res = None
    for z, block in enumerate(blocks):
        vert_res, hor_res = find_prev(block)
        if vert_res:
            part1 += vert_res 
        else:
            part1 += hor_res * 100
        res = None
        for i, line in enumerate(block):
            for j, c in enumerate(line):
                if c == '.':
                    block = change_char(block, i, j, '#')
                    res = find_line_smudge(block, vert_res, hor_res)
                    if res is not None:
                        part2 += res
                    block = change_char(block, i, j, '.')
                else:
                    block = change_char(block, i, j, '.')
                    res = find_line_smudge(block, vert_res, hor_res)
                    if res is not None:
                        part2 += res
                    block = change_char(block, i, j, '#')
                if res:
                    break
            if res:
                break
    print('Part 1:', part1)
    print('Part 2:', part2)

def main():
    blocks = parse_input('input')
    find_line(blocks)
    
if __name__ == "__main__":
    main()