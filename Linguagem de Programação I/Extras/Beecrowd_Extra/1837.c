#include <stdio.h>

int main() {
    int a, b, r, q;
    scanf("%d %d", &a, &b);
    for (r = 0; r < abs(b); r++) {
        if ((a - r) % b == 0) {
            q = (a - r) / b;
            break;
        }
    }
    printf("%d %d\n", q, r);
    return 0;
}