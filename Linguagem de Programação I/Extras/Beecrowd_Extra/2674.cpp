#include <iostream>
#include <cmath>
#include <string>

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

bool is_super(int n) {
    std::string prime_digits = "2357";
    std::string str_n = std::to_string(n);

    for (char c : str_n) {
        if (prime_digits.find(c) == std::string::npos) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    while (std::cin >> n) {
        if (is_prime(n)) {
            if (is_super(n)) {
                std::cout << "Super\n";
            } else {
                std::cout << "Primo\n";
            }
        } else {
            std::cout << "Nada\n";
        }
    }
    return 0;
}