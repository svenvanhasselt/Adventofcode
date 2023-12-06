file = open('../Input/day6_2', 'r')

Lines = file.readlines()

for index, line in enumerate(Lines):
    if index == 0:
        time_int = int("".join(char for char in line.split() if char.isdigit()))
    else:
        dist_int = int("".join(char for char in line.split() if char.isdigit()))

hold = 1
count = 0
while hold != time_int:
    speed = time_int - hold
    tot_dist = hold * speed
    if tot_dist > dist_int:
        count += 1
    hold += 1
print(count)