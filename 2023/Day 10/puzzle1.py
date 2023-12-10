def parse_input(input):
    file = open(input, 'r')

    lines = file.readlines()

    map = []
    for line in lines:
        line = line.replace('\n', '')
        map.append(list(line))
    return map

def find_start(map):
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if col == 'S':
                return x, y

def move(map, start, movement):
    cur_row, cur_col = start
    directions = {
    'D': (cur_row, cur_col + 1),
    'U': (cur_row, cur_col - 1),
    'R': (cur_row + 1, cur_col),
    'L': (cur_row - 1, cur_col)
}
    new_position = directions.get(movement, start)
    if 0 <= start[0] < len(map[0]) and 0 <= start[1] < len(map):
        return new_position
    else:
        return start

def check_movements(m_p):
    if m_p == '7':
        return "DL"
    if m_p == '|':
        return "UD"
    if m_p == 'L':
        return "UR"
    if m_p == '-':
        return "RL"
    if m_p == 'J':
        return "UL"
    if m_p == 'F':
        return "RD"
    if m_p == 'S':
        return "RLUD"

def find_next(map, start, route):
    m_p = map[start[1]][start[0]]
    movements = check_movements(m_p)
    p = start
    for m in movements:
        p = move(map, p, m)  
        m_p = map[p[1]][p[0]]
        if m_p == 'S' and len(route) != 1:
            return p
        if [*p] in route:
            p = start
            continue
        if m == 'R' and (m_p == '-' or m_p == '7' or m_p == 'J'):
            return p
        if m == 'L' and (m_p == '-' or m_p == 'F' or m_p == 'L'):
            return p
        if m == 'D' and (m_p == '|' or m_p == 'L' or m_p == 'J'):
            return p
        if m == 'U' and (m_p == '|' or m_p == 'F' or m_p == '7'):
            return p
        p = start

def walk_loop(map, start):
    route = []
    count = 0
    n_p = find_next(map, start, route)
    m_p = map[n_p[1]][n_p[0]]
    route.append([*n_p])
    count += 1
    while m_p != 'S':
        n_p = find_next(map, n_p, route)
        route.append([*n_p])
        count += 1
        m_p = map[n_p[1]][n_p[0]]
        if m_p == 'S':
            break
    
    print('Part 1:', count / 2)
    return route

def part2(route, map):
    from matplotlib.path import Path
    sum = 0
    p = Path(route)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if [x, y] in route:
                continue
            if p.contains_point((x, y)):
                sum += 1
    print('Part 2:', sum)


def solution(map):
    start = find_start(map)
    route = walk_loop(map, start)
    part2(route, map)

def main():
    map = parse_input('input')
    solution(map)

if __name__ == "__main__":
    main()