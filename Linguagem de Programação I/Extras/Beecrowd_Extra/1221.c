#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#define MAX 65536

bool C[MAX];
int primos[MAX];
int total_primos = 0;

void Crivo(int n) {
    for (int i = 0; i < n; i++) {
        C[i] = true;
    }

    C[1] = false;
    primos[total_primos++] = 2;

    for (int i = 4; i < n; i += 2) {
        C[i] = false;
    }

    for (int i = 3; i < n; i += 2) {
        if (C[i]) {
            primos[total_primos++] = i;

            for (int j = i * 3; j < n; j += 2 * i) {
                C[j] = false;
            }
        }
    }
}

bool ehPrimo(int n) {
    int limite = (int) ceil(sqrt(n));

    for (int i = 0; i < total_primos; i++) {
        if (primos[i] > limite) {
            return true;
        } else if (n % primos[i] == 0) {
            return (n == primos[i]);
        }
    }

    return true;
}

int main() {
    Crivo(MAX);

    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int X;
        scanf("%d", &X);

        printf(ehPrimo(X) ? "Prime\n" : "Not Prime\n");
    }

    return 0;
}