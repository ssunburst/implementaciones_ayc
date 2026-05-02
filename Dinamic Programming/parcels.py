def solution(C):
    n = len(C)
    min_cost = None
    if n < 2:
        min_cost = C[0]
    else:
        costs = [0] * n
        costs[0] = C[0]
        costs[1] = C[1]
        for i in range(2, n):
            costs[i] = C[i] + min(costs[i-1], costs[i-2])
        min_cost = costs[n-1]
    return min_cost

parcels_costs = [10, 5, 12, 1, 1, 20, 12, 7, 3]
print(solution(parcels_costs))