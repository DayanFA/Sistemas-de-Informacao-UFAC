#include <stdio.h>
#include <string.h>

int main() {
    int n, l, c;
    while (scanf("%d %d %d", &n, &l, &c) == 3) {
        char words[n][100];
        for (int i = 0; i < n; i++) {
            scanf("%s", words[i]);
        }
        int lines = 0, chars = 0, pages = 0;
        for (int i = 0; i < n; i++) {
            int len = strlen(words[i]);
            if (chars + len > c) {
                chars = 0;
                lines++;
                if (lines == l) {
                    lines = 0;
                    pages++;
                }
            }
            chars += len + 1;
        }
        if (chars || lines) {
            pages++;
        }
        printf("%d\n", pages);
    }
    return 0;
}