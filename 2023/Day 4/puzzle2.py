file = open('../Input/day4_2', 'r')

Lines = file.readlines()

index = 0
game = [1] * len(Lines)
while index < len(Lines):
    split_line = Lines[index].split(": ")
    split_game = split_line[1].split(" | ")
    game_card = [int(num) for num in split_game[0].split()]
    my_cards = [int(num) for num in split_game[1].split()]
    count = 0
    for num in game_card:
        for num2 in my_cards:
            if num == num2:
                count += 1
    repeat = game[index]
    temp = count
    while repeat > 0:
        count = temp
        while count > 0:
            game[index + count] += 1
            count -= 1
        repeat -= 1
    index += 1
print(sum(game))
file.close()