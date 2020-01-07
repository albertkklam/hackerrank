#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int queries, query_type, mark;
    string name;
    map<string, int> m;
    cin >> queries;
    for(int i; i < queries; i++) {
        cin >> query_type >> name;
        if(query_type == 1) {
            cin >> mark;
            m[name] += mark;
        }
        else if (query_type == 2) {
            m.erase(name);
        }
        else {
            if(m.find(name) == m.end()) {
                cout << 0 << endl;
            }
            else {
                cout << m[name] << endl;
            }
        }
    }
}