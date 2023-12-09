import fileinput

tot = 0
firsts = []
for d in [[int(i) for i in ln.split()] for ln in fileinput.input()]:
    subfirst = []
    while d:
        tot += d[-1]
        subfirst.append(d[0])
        d = [j - i for i, j in zip(d, d[1:])]
    firsts.append(subfirst)

print('P1 =', tot)
tot = [(-n if i % 2 else n) for d in firsts for i, n in enumerate(d)]
print('P2 =', sum(tot))