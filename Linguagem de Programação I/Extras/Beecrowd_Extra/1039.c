#include <stdio.h>
#include <math.h>

int main() {
    int R1, X1, Y1, R2, X2, Y2;
    while (scanf("%d %d %d %d %d %d", &R1, &X1, &Y1, &R2, &X2, &Y2) != EOF) {
        double distance = sqrt(pow(X2 - X1, 2) + pow(Y2 - Y1, 2));
        if (R1 >= distance + R2) {
            printf("RICO\n");
        } else {
            printf("MORTO\n");
        }
    }
    return 0;
}