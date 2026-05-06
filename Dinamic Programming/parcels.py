def solution(C):
    n = len(C)
    min_cost = None
    if n < 2:
        min_cost = C[0]
    else:
        costs = [0] * n
        for i in range(0, n):
            costs[i] = C[i] + min(costs[i-1] if i > 0 else 0, costs[i-2] if i > 1 else 0)
        min_cost = costs[n-1]
    return min_cost

def solution_opt(C):

    def build_solution(O):
        n = len(O)
        order = [n]
        while order[-1] > 2:
            order.append(O[order[-1]-1] + 1)
        order.reverse()
        return order
    
    n = len(C)
    parcels_order = [0] * n
    min_cost = None

    if n < 2:
        min_cost = C[0]
    else:
        prev_1 = 0
        prev_2 = 0
        for i in range(0, n):
            min_cost = C[i]
            if (prev_1 <= prev_2):
                parcels_order[i] = i - 1
                min_cost += prev_1
            else:
                parcels_order[i] = i - 2
                min_cost += prev_2
            prev_1, prev_2 = min_cost, prev_1

    return min_cost, build_solution(parcels_order)

parcels_costs = [10, 5, 12, 1, 1, 20, 12, 7, 3]
print("\nCostos de acceso a pacelas\n")
for i in range(len(parcels_costs)):
    print(i+1, ":\t", parcels_costs[i], sep="")

print("\nCosto mínimo de acceso:", solution_opt(parcels_costs))