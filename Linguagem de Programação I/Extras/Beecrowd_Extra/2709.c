#include <stdio.h>
#include <stdbool.h>

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
    int p = 3;
    while (p * p <= n) {
        if (n % p == 0) {
            return false;
        }
        p += 2;
    }
    return true;
}

int main() {
    int M, N;
    while (scanf("%d", &M) != EOF) {
        int coins[M];
        for (int i = 0; i < M; i++) {
            scanf("%d", &coins[i]);
        }
        scanf("%d", &N);
        int sum_coins = 0;
        for (int i = M - 1; i >= 0; i -= N) {
            sum_coins += coins[i];
        }
        if (is_prime(sum_coins)) {
            printf("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");
        } else {
            printf("Bad boy! I’ll hit you.\n");
        }
    }
    return 0;
}