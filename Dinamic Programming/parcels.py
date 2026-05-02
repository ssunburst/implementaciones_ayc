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
    n = len(C)
    min_cost = None
    if n < 2:
        min_cost = C[0]
    else:
        prev_1 = 0
        prev_2 = 0
        min_cost = float('inf') # Cualquier valor sirve; es inmediatamente actualizado
        for i in range(0, n):
            min_cost = C[i] + min(prev_1, prev_2)
            prev_1, prev_2 = min_cost, prev_1
    return min_cost

parcels_costs = [10, 5, 12, 1, 1, 20, 12, 7, 3]
print("Costos de acceso a pacelas\n")
for i in range(len(parcels_costs)):
    print(i+1, ":\t", parcels_costs[i], sep="")

print("\nCosto mínimo de acceso:", solution_opt(parcels_costs))