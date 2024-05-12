#include <iostream>
#include <vector>
#include <string>

int main() {
    int n, l, c;
    while (std::cin >> n >> l >> c) {
        std::vector<std::string> words(n);
        for (int i = 0; i < n; i++) {
            std::cin >> words[i];
        }
        int lines = 0, chars = 0, pages = 0;
        for (int i = 0; i < n; i++) {
            int len = words[i].size();
            if (chars + len > c) {
                chars = 0;
                lines++;
                if (lines == l) {
                    lines = 0;
                    pages++;
                }
            }
            chars += len + 1;
        }
        if (chars || lines) {
            pages++;
        }
        std::cout << pages << std::endl;
    }
    return 0;
}