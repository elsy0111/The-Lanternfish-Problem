#include <iostream>
#include <vector>
#include <cmath>
// Ref : https://github.com/atcoder/ac-library
#include <atcoder/modint>
#define int long long
using namespace std;
using namespace atcoder;
using mint = modint998244353;

const int M = 9;

vector<vector<mint>> DP = {
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

vector<vector<mint>> matrixMult(vector<vector<mint>>& A, vector<vector<mint>>& B) {
    int Bx = B.size();

    vector<vector<mint>> result(M, vector<mint>(Bx, 0));

    for (int i = 0; i < M; ++i) { 			// A_row
        for (int j = 0; j < Bx; ++j) { 		// B_col
            for (int k = 0; k < M; ++k) { 	// A_col = B_row
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}

signed main() {
    int N, T;
    cin >> N >> T;

	// Ans_0 (= V)
    vector<vector<mint>> Ans(M, vector<mint>(1,0));
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
        cout << Ans[i][0].val() << endl;
    }

    return 0;
}
