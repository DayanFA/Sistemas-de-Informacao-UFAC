#include <stdio.h>

int main() {
    int sh, sm, eh, em;
    scanf("%d %d %d %d", &sh, &sm, &eh, &em);
    int st = sh * 60 + sm;
    int et = eh * 60 + em;
    int d = et - st;
    if (d <= 0) {
        d += 24 * 60;
    }
    int h = d / 60;
    int m = d % 60;
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
    return 0;
}