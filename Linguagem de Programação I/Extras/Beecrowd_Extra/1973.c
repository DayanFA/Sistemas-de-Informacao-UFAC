#include <stdio.h>

int main() {
    int n, i = 0, count = 0;
    long long int sum = 0;  
    scanf("%d", &n);

    int carneiros[n];
    int estrelas_atacadas[n];

    for (int j = 0; j < n; ++j) {
        scanf("%d", &carneiros[j]);
        estrelas_atacadas[j] = 0;
    }

    while (0 <= i && i < n) {
        estrelas_atacadas[i] = 1;
        if (carneiros[i] % 2 == 0) {
            carneiros[i] = carneiros[i] > 0 ? carneiros[i] - 1 : 0;
            i -= 1;
        } else {
            carneiros[i] = carneiros[i] > 0 ? carneiros[i] - 1 : 0;
            i += 1;
        }
    }

    for (int j = 0; j < n; ++j) {
        count += estrelas_atacadas[j];
        sum += carneiros[j];  
    }

    printf("%d %lld\n", count, sum);  

    return 0;
}