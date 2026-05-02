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

def solution_opt(C):
    n = len(C)
    min_cost = None
    if n < 2:
        min_cost = C[0]
    else:
        prev_1 = C[1]
        prev_2 = C[0]
        min_cost = min(prev_1, prev_2)
        for i in range(2, n):
            min_cost = C[i] + min(prev_1, prev_2)
            prev_1, prev_2 = min_cost, prev_1
    return min_cost

parcels_costs = [10, 5, 12, 1, 1, 20, 12, 7, 3]
print(solution_opt(parcels_costs))