import numpy as np

N,T = map(int,input().split())
M = 9

cnt = [[0] for _ in range(M)]
for A in map(int,input().split()):
	cnt[A][0] += 1

ans = np.matrix(cnt)

dp = np.matrix([
	[0,1,0,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0,0],
	[0,0,0,1,0,0,0,0,0],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,1,0,0,0],
	[0,0,0,0,0,0,1,0,0],
	[1,0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0]])

MOD = 998244353

while T:
	if T&1:
		ans = np.mod(dp.dot(ans), MOD)
	dp = np.mod(dp.dot(dp), MOD)
	T >>= 1

ans = ans.tolist()

for i in range(9):
    print(ans[i][0])
