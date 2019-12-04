#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
   stringstream ss(str);
   vector<int> vec;
   char comma;
   int val;

   while(ss >> val) {
       vec.push_back(val);
       ss >> comma;
   }

   return vec;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}

