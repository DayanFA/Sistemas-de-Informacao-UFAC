#include <stdio.h>
#include <stdlib.h>

int compare(const void * a, const void * b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int T = 1;
    int N, Q;
    while (scanf("%d %d", &N, &Q), N || Q) {
        int marmores[N];
        for (int i = 0; i < N; i++) {
            scanf("%d", &marmores[i]);
        }

        qsort(marmores, N, sizeof(int), compare);

        printf("CASE# %d:\n", T++);
        for (int i = 0; i < Q; i++) {
            int consulta;
            scanf("%d", &consulta);

            int *resposta = (int*) bsearch(&consulta, marmores, N, sizeof(int), compare);
            if (resposta) {
                while (resposta > marmores && *(resposta - 1) == consulta) {
                    resposta--;
                }
                printf("%d found at %ld\n", consulta, resposta - marmores + 1);
            } else {
                printf("%d not found\n", consulta);
            }
        }
    }
    return 0;
}