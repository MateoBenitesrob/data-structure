N, M, K = map(int, input().split())

P = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    fila = list(map(int, input().split()))
    for j in range(1, M + 1):
        val = fila[j - 1]
        P[i][j] = val + P[i][j - 1] + P[i - 1][j] - P[i - 1][j - 1] 
def calcular_subrectangulo(P, N, M, K):
    max_suma = -float("inf")
    for f2 in range(K, N + 1):
        for c2 in range(K, M + 1):
            f1 = f2 - K + 1
            c1 = c2 - K + 1
            Z = P[f2][c2] - P[f1 - 1][c2] - P[f2][c1 - 1] + P[f1 - 1][c1 - 1]
            if Z > max_suma:
                max_suma = Z
    return max_suma
print((calcular_subrectangulo(P, N, M, K)))