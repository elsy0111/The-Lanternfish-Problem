M = 9
MOD = 998244353
DP = [[0,1,0,0,0,0,0,0,0],
	  [0,0,1,0,0,0,0,0,0],
	  [0,0,0,1,0,0,0,0,0],
	  [0,0,0,0,1,0,0,0,0],
	  [0,0,0,0,0,1,0,0,0],
	  [0,0,0,0,0,0,1,0,0],
	  [1,0,0,0,0,0,0,1,0],
	  [0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0]]

def MatrixMult(A, B, MOD):
    Bx = len(B[0])
    res = [[0 for _ in range(Bx)]for _ in range(M)]
    for i in range(M):
        for j in range(Bx):
            for k in range(M):
                res[i][j] += A[i][k] * B[k][j]
                res[i][j] %= MOD
    return res

N,T = map(int,input().split())
A = list(map(int,input().split()))

Ans = [[0] for _ in range(M)]
for i in range(N):
	Ans[A[i]][0] += 1

while T:
	if T&1:
		Ans = MatrixMult(DP, Ans, MOD)
	DP = MatrixMult(DP, DP, MOD)
	T >>= 1

for i in range(9):
    print(Ans[i][0])
