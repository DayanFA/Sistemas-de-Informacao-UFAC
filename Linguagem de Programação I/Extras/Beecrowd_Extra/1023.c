#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int key;
    int value;
} pair;

int compare(const void *a, const void *b) {
    return ((pair *)a)->key - ((pair *)b)->key;
}

int main() {
    int T = 0;
    int N;
    while (scanf("%d", &N) != EOF && N != 0) {
        if (T > 0) {
            printf("\n");
        }

        int totalX = 0, totalY = 0;
        pair consumos[1000] = {0};
        int numPairs = 0;
        for (int i = 0; i < N; i++) {
            int X, Y;
            scanf("%d %d", &X, &Y);
            totalX += X;
            totalY += Y;
            int key = Y / X;
            int j;
            for (j = 0; j < numPairs; j++) {
                if (consumos[j].key == key) {
                    consumos[j].value += X;
                    break;
                }
            }
            if (j == numPairs) {
                consumos[numPairs].key = key;
                consumos[numPairs].value = X;
                numPairs++;
            }
        }

        T += 1;
        printf("Cidade# %d:\n", T);

        qsort(consumos, numPairs, sizeof(pair), compare);
        for (int i = 0; i < numPairs; i++) {
            printf("%d-%d ", consumos[i].value, consumos[i].key);
        }
        printf("\n");

        double consumo_medio = floor((100.0 * totalY) / totalX) / 100;
        printf("Consumo medio: %.2f m3.\n", consumo_medio);
    }
    return 0;
}