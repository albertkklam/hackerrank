#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q, k, i, j, val;
    cin >> n >> q;
    vector<vector<int>> vec;

    for(int i_iter = 0; i_iter < n; i_iter++) {
        cin >> k;
        vector<int> v;
        for (int j_iter = 0; j_iter < k; j_iter++) {
            cin >> val;
            v.push_back(val);
        }
        vec.push_back(v);
    }

    for (int k_iter = 0; k_iter < q; k_iter++) {
        cin >> i >> j;
        cout << vec[i][j] << endl;
    }

    return 0;
}