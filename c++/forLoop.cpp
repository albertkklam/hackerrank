#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a;
    int b;
    string message[9] = {"one", "two", "three", "four", "five",
                          "six", "seven", "eight", "nine"};
    cin >> a >> b;
    for(int n = a; n <= b; n++) {
        if(n >= 1 && n <= 9) {
            cout << message[n-1] << endl;
        }
        else if (n > 9 && n % 2 == 0) {
            cout << "even" << endl;
        }
        else {
            cout << "odd" << endl;
        }
    }
    return 0;
}
