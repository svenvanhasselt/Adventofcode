import re

def parse_input(input):
    file = open(input, 'r')

    lines = file.readlines()
    seq = []
    seq2 = []
    for line in lines:
        seq.extend(line.split(','))
    
    for s in seq:
        split = re.split(r'[- =]', s)
        split = [s for s in split if s]
        seq2.append(split)

    return seq, seq2

def calc_current(s):
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current

def process_seq(seq):
    current_total = 0
    for s in seq:
        current_total += calc_current(s)
    print('Part 1:', current_total)

def process_part2(seq):
    box_list = {}
    for s in seq:
        box = calc_current(s[0])
        if len(s) == 2:
            dup = None
            if box in box_list:
                dup = next((index for index, sublist in enumerate(box_list[box]) if sublist[0] == s[0]), None)
            if dup is not None:
                box_list[box][dup][1] = s[1]
            else:
                box_list.setdefault(box, []).append(s)
        else:
            if box in box_list:
                rem = next((index for index, sublist in enumerate(box_list[box]) if sublist[0] == s[0]), None)
                if rem is not None:
                    box_list[box].pop(rem)
    return(box_list)

def calc_part2(box_list):
    total = 0
    for box_val, box in box_list.items():
        for i, lens in enumerate(box):
            total += (box_val + 1) * (i + 1) * int(lens[1])
    print('Part 2:',total)

def main():
    part1, part2 = parse_input('input')
    process_seq(part1)
    box_list = process_part2(part2)
    calc_part2(box_list)
if __name__ == "__main__":
    main()