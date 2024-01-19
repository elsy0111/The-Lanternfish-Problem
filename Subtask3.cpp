#include <iostream>
#include <vector>
#include <cmath>
#define int long long
using namespace std;

const int MOD = 998244353;
const int M = 9;

vector<vector<int>> DP = {
    {0, 1, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 1, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 1, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 1, 0, 0},
    {1, 0, 0, 0, 0, 0, 0, 1, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0}
};

vector<vector<int>> matrixMult(vector<vector<int>>& A, vector<vector<int>>& B) {
    int Bx = B.size();

    vector<vector<int>> result(M, vector<int>(Bx, 0));

    for (int i = 0; i < M; ++i) { 			// A_row
        for (int j = 0; j < Bx; ++j) { 		// B_col
            for (int k = 0; k < M; ++k) { 	// A_col = B_row
                result[i][j] += (A[i][k] % MOD * B[k][j] % MOD) % MOD;
				result[i][j] %= MOD;
            }
        }
    }

    return result;
}

signed main() {
    int N, T;
    cin >> N >> T;

	// Ans_0 (= V)
    vector<vector<int>> Ans(M, vector<int>(1,0));
    for (int i = 0; i < N; ++i) {
        int A; cin >> A;
        Ans[A][0] += 1;
    }

    while (T) {
        if (T & 1) {
            Ans = matrixMult(DP, Ans);
        }
        DP = matrixMult(DP, DP);
        T >>= 1;
    }

    for (int i = 0; i < 9; ++i) {
        cout << Ans[i][0] << endl;
    }

    return 0;
}
