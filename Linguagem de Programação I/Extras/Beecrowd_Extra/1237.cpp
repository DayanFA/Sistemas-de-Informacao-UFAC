#include <iostream>
#include <vector>
#include <string>

int longest_common_substring(std::string A, std::string B) {
    int n = A.size(), m = B.size();
    std::vector<std::vector<int>> T(n + 1, std::vector<int>(m + 1, 0));
    int result = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (A[i - 1] == B[j - 1]) {
                T[i][j] = T[i - 1][j - 1] + 1;
                result = std::max(result, T[i][j]);
            }
        }
    }

    return result;
}

int main() {
    std::string A, B;
    while (std::getline(std::cin, A) && std::getline(std::cin, B)) {
        std::cout << longest_common_substring(A, B) << std::endl;
    }
    return 0;
}