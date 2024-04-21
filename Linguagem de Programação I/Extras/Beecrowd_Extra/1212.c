#include <stdio.h>
#include <string.h>

int main() {
    char a[11], b[11];
    while (1) {
        scanf("%s %s", a, b);
        if (a[0] == '0' && b[0] == '0' && a[1] == '\0' && b[1] == '\0') {
            break;
        }

        int carry = 0, c = 0;
        int len_a = strlen(a), len_b = strlen(b);
        while (len_a < len_b) {
            memmove(a + 1, a, len_a + 1);
            a[0] = '0';
            len_a++;
        }
        while (len_b < len_a) {
            memmove(b + 1, b, len_b + 1);
            b[0] = '0';
            len_b++;
        }

        for (int i = len_a - 1; i >= 0; i--) {
            if ((a[i] - '0' + b[i] - '0' > 9) || (a[i] - '0' + b[i] - '0' + c > 9)) {
                carry++;
                c = 1;
            } else {
                c = 0;
            }
        }

        if (carry == 0) {
            printf("No carry operation.\n");
        } else if (carry == 1) {
            printf("1 carry operation.\n");
        } else {
            printf("%d carry operations.\n", carry);
        }
    }
    return 0;
}