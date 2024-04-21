#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void * a, const void * b) {
    return *(char*)a - *(char*)b;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int _ = 0; _ < t; _++) {
        char n[1000];
        scanf("%s", n);
        int len = strlen(n);
        qsort(n, len, sizeof(char), compare);
        if (n[0] == '0') {
            for (int i = 1; i < len; i++) {
                if (n[i] != '0') {
                    char temp = n[0];
                    n[0] = n[i];
                    n[i] = temp;
                    break;
                }
            }
        }
        printf("%s\n", n);
    }
    return 0;
}