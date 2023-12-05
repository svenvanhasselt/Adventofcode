def check_next(seed, lists):
    for list in lists:
        min = list[1]
        max = list[1] + list[2]
        match = list[0] - list[1]
        if seed >= min and seed <= max:
            seed += match
            return (seed)
    return (seed)
            
file = open('../Input/day5_1', 'r')

Lines = file.readlines()

section = 0
s_s = []
s_f = []
f_w = []
w_l = []
l_t = []
t_h = []
h_l = []
for line in Lines:
    if line == '\n':
       section += 1
    if section == 0:
        seed_range = [int(char) for char in line.split() if char.isdigit()]
    elif section == 1 and line[0].isdigit():
        s_s.append([int(char) for char in line.split() if char.isdigit()])
    elif section == 2 and line[0].isdigit():
        s_f.append([int(char) for char in line.split() if char.isdigit()])
    elif section == 3 and line[0].isdigit():
        f_w.append([int(char) for char in line.split() if char.isdigit()])
    elif section == 4 and line[0].isdigit():
        w_l.append([int(char) for char in line.split() if char.isdigit()])
    elif section == 5 and line[0].isdigit():
        l_t.append([int(char) for char in line.split() if char.isdigit()])
    elif section == 6 and line[0].isdigit():
        t_h.append([int(char) for char in line.split() if char.isdigit()])
    elif section == 7 and line[0].isdigit():
        h_l.append([int(char) for char in line.split() if char.isdigit()])

seeds = []
index = 0
check = 0
while index < len(seed_range):
    print(index)
    i = 0
    while index + 1 < len(seed_range) and i < seed_range[index + 1]:
        seed = check_next(seed_range[index] + i, s_s)
        seed = check_next(seed, s_f)
        seed = check_next(seed, f_w)
        seed = check_next(seed, w_l)
        seed = check_next(seed, l_t)
        seed = check_next(seed, t_h)
        seed = check_next(seed, h_l)
        if check == 0:
            final = seed
            check = 1
        elif seed < final:
            final = seed
        i += 1
    index += 2

print(final)