import sys
n, m = list(map(int,sys.stdin.readline().split(" ")))

dna = []
for i in range(n):
    dna.append(input(""))
    # dna = [input() for _ in range(n)]
def to_char(a, t, g, c, max_count):
    if max_count == a:
        return 'A'
    elif max_count == c:
        return 'C'
    elif max_count == g:
        return 'G'
    else:
        return 'T'

hd = 0
for i in range(m):
    a = t = g = c = 0
    for j in range(n):
        if dna[j][i] == 'A':
            a += 1
        elif dna[j][i] == 'T':
            t += 1
        elif dna[j][i] == 'G':
            g += 1
        else:
            c += 1
    max_count = max(a, c, g, t)
    hd += (n - max_count)
    print(to_char(a, t, g, c, max_count), end='')
print()
print(hd)
