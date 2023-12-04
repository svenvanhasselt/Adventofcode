file = open('../Input/day4_1', 'r')

Lines = file.readlines()

sum = 0
for line in Lines:
    split_line = line.split(": ")
    split_game = split_line[1].split(" | ")
    game_card = [int(num) for num in split_game[0].split()]
    my_cards = [int(num) for num in split_game[1].split()]
    count = 0
    for num in game_card:
        for num2 in my_cards:
            if num == num2:
                count += 1
    if (count > 0):
        sum += 2 ** (count - 1)
print(sum)