#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

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
    char prime_digits[] = "2357";
    char str_n[20];
    sprintf(str_n, "%d", n);

    for (int i = 0; i < strlen(str_n); i++) {
        if (strchr(prime_digits, str_n[i]) == NULL) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    while (scanf("%d", &n) != EOF) {
        if (is_prime(n)) {
            if (is_super(n)) {
                printf("Super\n");
            } else {
                printf("Primo\n");
            }
        } else {
            printf("Nada\n");
        }
    }
    return 0;
}