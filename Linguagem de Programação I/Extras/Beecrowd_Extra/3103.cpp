#include <iostream>
#include <algorithm>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (int _ = 0; _ < t; _++) {
        std::string n;
        std::cin >> n;
        std::sort(n.begin(), n.end());
        if (n[0] == '0') {
            for (int i = 1; i < n.size(); i++) {
                if (n[i] != '0') {
                    std::swap(n[0], n[i]);
                    break;
                }
            }
        }
        std::cout << n << std::endl;
    }
    return 0;
}