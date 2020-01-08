#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, val, q, y;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++) {
        cin >> val;
        v.push_back(val);
    }
    cin >> q;
    for(int i = 0; i < q; i++) {
        cin >> y;
        vector<int>::iterator low;
        low = lower_bound(v.begin(), v.end(), y);
        if(v[low - v.begin()] == y) {
            cout << "Yes" << " " << low - v.begin() + 1 << endl;
        }
        else {
            cout << "No" << " " << low - v.begin() + 1 << endl;
        }
    }
}
