M = [1, 5, 10, 25, 50, 100, 200]

def coins(C): # C lista de denominaciones, M monto a pagar
    global M
    ways = [[0] * (C+1) for i in range(len(M))]
    for i in range(len(M)):
        ways[i][0] = 1
    
    for i in range(len(M) - 1, -1, -1): # Se empieza usando únicamente el último monto
        for j in range(1, C + 1):       # La columna 0 ya está completa (caso base)
            total_ways = 0
            for k in range(i, len(M)):
                total_ways += ways[k][j - M[k]] if (j - M[k] >= 0) else 0
            ways[i][j] = total_ways    

    return ways[0][C]

print(coins(12))