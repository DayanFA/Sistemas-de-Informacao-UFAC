#include <stdio.h>
#include <string.h>

int longest_common_substring(char *A, char *B) {
    int n = strlen(A), m = strlen(B);
    int T[n + 1][m + 1];
    memset(T, 0, sizeof(T));
    int result = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (A[i - 1] == B[j - 1]) {
                T[i][j] = T[i - 1][j - 1] + 1;
                if (result < T[i][j]) {
                    result = T[i][j];
                }
            }
        }
    }

    return result;
}

int main() {
    char A[1000], B[1000];
    while (fgets(A, sizeof(A), stdin) != NULL && fgets(B, sizeof(B), stdin) != NULL) {
        A[strcspn(A, "\n")] = 0;
        B[strcspn(B, "\n")] = 0;
        printf("%d\n", longest_common_substring(A, B));
    }
    return 0;
}