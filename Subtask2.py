N, T = map(int,input().split())
A = list(map(int,input().split()))

MOD = 998244353

Ans = [0] * 9
for i in range(N):
    Ans[A[i]] += 1

for _ in range(T):
    Ans_before = Ans[:]
    Ans[0] = Ans_before[1] % MOD
    Ans[1] = Ans_before[2] % MOD
    Ans[2] = Ans_before[3] % MOD
    Ans[3] = Ans_before[4] % MOD
    Ans[4] = Ans_before[5] % MOD
    Ans[5] = Ans_before[6] % MOD
    Ans[6] =(Ans_before[7] + Ans_before[0]) % MOD
    Ans[7] = Ans_before[8] % MOD
    Ans[8] = Ans_before[0] % MOD

for i in range(9):
    print(Ans[i])
