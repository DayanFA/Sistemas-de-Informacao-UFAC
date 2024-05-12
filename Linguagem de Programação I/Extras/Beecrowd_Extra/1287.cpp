#include <iostream>
#include <string>
#include <cstdlib>

int main() {
    std::string s;
    while (std::getline(std::cin, s)) {
        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] == 'O' || s[i] == 'o') {
                s[i] = '0';
            } else if (s[i] == 'l') {
                s[i] = '1';
            } else if (s[i] == ',' || s[i] == ' ') {
                s.erase(i, 1);
                --i;
            }
        }

        char* end;
        long long num = std::strtoll(s.c_str(), &end, 10);
        if (*end != '\0' || num > 2147483647 || s.empty()) {
            std::cout << "error\n";
        } else {
            std::cout << num << "\n";
        }
    }

    return 0;
}