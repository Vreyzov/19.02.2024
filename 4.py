table = [input().split() for _ in range(int(input())-1)]
indices = tuple(map(int, input().split()))

res = []
for s, i in zip(zip(*table), indices):
    try:
        res.append(''.join([x[i] for x in s]))
    except Exception:
        break
print(*sorted(set(res)), sep='; ', end='.')