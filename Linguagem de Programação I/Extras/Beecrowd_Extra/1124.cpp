#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int L, C, R1, R2;

    while (true) {
        cin >> L >> C >> R1 >> R2;
        if (L == 0 && C == 0 && R1 == 0 && R2 == 0)
            break;

        if (2 * max(R1, R2) > min(L, C)) {
            cout << "N" << endl;
            continue;
        }

        if (pow(R1 + R2, 2) <= pow(L - R1 - R2, 2) + pow(C - R1 - R2, 2))
            cout << "S" << endl;
        else
            cout << "N" << endl;
    }

    return 0;
}