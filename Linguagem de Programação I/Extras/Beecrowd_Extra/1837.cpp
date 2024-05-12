#include <iostream>
#include <cmath>

int main() {
    int a, b, r, q;
    std::cin >> a >> b;
    for (r = 0; r < std::abs(b); r++) {
        if ((a - r) % b == 0) {
            q = (a - r) / b;
            break;
        }
    }
    std::cout << q << " " << r << std::endl;
    return 0;
}