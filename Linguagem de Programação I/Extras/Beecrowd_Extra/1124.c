#include <stdio.h>
#include <math.h>

int main() {
    int L, C, R1, R2;

    while (1) {
        scanf("%d %d %d %d", &L, &C, &R1, &R2);
        if (L == 0 && C == 0 && R1 == 0 && R2 == 0)
            break;

        if (2 * fmax(R1, R2) > fmin(L, C)) {
            printf("N\n");
            continue;
        }

        if (pow(R1 + R2, 2) <= pow(L - R1 - R2, 2) + pow(C - R1 - R2, 2))
            printf("S\n");
        else
            printf("N\n");
    }

    return 0;
}