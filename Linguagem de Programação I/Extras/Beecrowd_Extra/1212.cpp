#include <iostream>
#include <string>

using namespace std;

int main() {
    while (true) {
        string a, b;
        cin >> a >> b;
        int carry = 0;
        int c = 0;
        if (a == "0" && b == "0") {
            break;
        }

        while (a.length() < b.length()) {
            a = '0' + a;
        }
        while (b.length() < a.length()) {
            b = '0' + b;
        }

        for (int i = a.length() - 1; i >= 0; i--) {
            if ((a[i] - '0' + b[i] - '0' > 9) || (a[i] - '0' + b[i] - '0' + c > 9)) {
                carry += 1;
                c = 1;
            } else {
                c = 0;
            }
        }

        if (carry == 0) {
            cout << "No carry operation.\n";
        } else if (carry == 1) {
            cout << "1 carry operation.\n";
        } else {
            cout << carry << " carry operations.\n";
        }
    }

    return 0;
}