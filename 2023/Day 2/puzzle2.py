file = open('input2', 'r')

Lines = file.readlines()
sum = 0
check = True
for game_number, line in enumerate(Lines):
    line = line.replace("\n", "")
    split_line = line.split(": ")
    split_set = split_line[1].split("; ")
    red = 0
    green = 0
    blue = 0
    for set in split_set:
        games = set.split(", ")
        for i in games:
            game = i.split(" ")
            if game[1] == "red" and int(game[0]) > red:
                red = int(game[0])
            if game[1] == "green" and int(game[0]) > green:
                green = int(game[0])
            if game[1] == "blue" and int(game[0]) > blue:
                blue = int(game[0])    
    sum += red * green * blue
print(sum)
file.close()