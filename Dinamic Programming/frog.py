def ways(d, S):
    ways = [0] * (d + 1)
    ways[0] = 1
    for i in range(1, d + 1):
        for jump in S:
            if i - jump >= 0:
                ways[i] += ways[i - jump]
    return ways[d]

d = 3
S = [1, 2]

print(ways(d, S))