#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, val;
    vector<int> v;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> val;
        v.push_back(val);
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    return 0;
}
