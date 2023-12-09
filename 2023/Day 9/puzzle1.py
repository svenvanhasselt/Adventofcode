import re

def parse_input(input):

    file = open(input, 'r')

    Lines = file.readlines()

    list1 = []
    list2 = []
    for line in Lines:
        numbers = [int(num) for num in re.findall(r'-?\d+', line)]
        num_cpy = numbers.copy()
        list1.append(numbers)
        num_cpy.reverse()
        list2.append(num_cpy)
    return list1, list2

def sub_list(line):
    res = []
    for i, num in enumerate(line):
        if i + 1 != len(line):
            res.append(line[i + 1] - line[i])
    return (res)

def solution(list):
    result = []
    for line in list:
        all_list = []
        all_list.append(line)
        all_list.append(sub_list(line))
        while True:
            all_list.append(sub_list(all_list[-1]))
            if all(x == 0 for x in all_list[-1]):
                all_list.reverse()
                for i, list in enumerate(all_list):
                    if i + 1 < len(all_list):
                        all_list[i + 1].append(all_list[i][-1] + all_list[i + 1][-1])
                result.append(all_list[-1][-1])
                break
    return sum(result)

def main():
    list1, list2 = parse_input('input')
    print('Part 1:', solution(list1))
    print('Part 2:', solution(list2))

if __name__ == "__main__":
    main()


