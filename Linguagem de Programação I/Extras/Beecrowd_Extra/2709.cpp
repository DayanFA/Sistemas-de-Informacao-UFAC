#include <iostream>
#include <vector>

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int p = 3; p * p <= n; p += 2) {
        if (n % p == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int M, N;
    while (std::cin >> M) {
        std::vector<int> coins(M);
        for (int i = 0; i < M; i++) {
            std::cin >> coins[i];
        }
        std::cin >> N;
        int sum_coins = 0;
        for (int i = M - 1; i >= 0; i -= N) {
            sum_coins += coins[i];
        }
        if (is_prime(sum_coins)) {
            std::cout << "You’re a coastal aircraft, Robbie, a large silver aircraft.\n";
        } else {
            std::cout << "Bad boy! I’ll hit you.\n";
        }
    }
    return 0;
}