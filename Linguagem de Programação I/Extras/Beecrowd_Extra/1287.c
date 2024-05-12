#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char s[1000];
    while (fgets(s, sizeof(s), stdin) != NULL) {
        for (int i = 0; i < strlen(s); i++) {
            if (s[i] == 'O' || s[i] == 'o') {
                s[i] = '0';
            } else if (s[i] == 'l') {
                s[i] = '1';
            } else if (s[i] == ',' || s[i] == ' ') {
                memmove(&s[i], &s[i + 1], strlen(s) - i);
                i--; 
            }
        }

        char *end;
        long long num = strtoll(s, &end, 10);
        if (*end != '\n' || num > 2147483647 || strlen(s) == 1) { 
            printf("error\n");
        } else {
            printf("%lld\n", num);
        }
    }

    return 0;
}