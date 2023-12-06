file = open('../Input/day6_1', 'r')

Lines = file.readlines()

sum = 0
for index, line in enumerate(Lines):
    if index == 0:
        time = [int(char) for char in line.split() if char.isdigit()]
    else:
        dist = [int(char) for char in line.split() if char.isdigit()]

list = []
for index, num in enumerate(time):
    hold = 1
    count = 0
    while hold != num:
        speed = num - hold
        tot_dist = hold * speed
        if tot_dist > dist[index]:
            count += 1
        hold += 1
    list.append(count)

result = 1
for num in list:
    result *= num
print(result)