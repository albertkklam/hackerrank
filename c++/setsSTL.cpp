#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int n;
    set<int> s;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int num, x;
        cin >> num >> x;
        if(num == 1) {
            s.insert(x);
        }
        else if(num == 2) {
            s.erase(x);
        }
        else {
            if(s.find(x) == s.end()) {
                cout << "No" << endl;
            }
            else {
                cout << "Yes" << endl;
            }
        }
    }
    return 0;
}

