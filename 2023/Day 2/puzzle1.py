file = open('input1', 'r')

Lines = file.readlines()
sum = 0
check = True
for game_number, line in enumerate(Lines):
    line = line.replace("\n", "")
    split_line = line.split(": ")
    split_set = split_line[1].split("; ")
    for set in split_set:
        games = set.split(", ")
        for i in games:
            game = i.split(" ")
            if game[1] == "red" and int(game[0]) > 12:
                check = False
            if game[1] == "green" and int(game[0]) > 13:
                check = False
            if game[1] == "blue" and int(game[0]) > 14:
                check = False
    if check == True:
        sum += game_number + 1
    else:
        check = True
print(sum)
file.close()