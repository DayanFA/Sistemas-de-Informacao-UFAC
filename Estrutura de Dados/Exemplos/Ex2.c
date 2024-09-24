#include <stdio.h>

// Função recursiva para calcular o produto de dois inteiros não negativos
int produto(int a, int b) {
    if (b == 0) {
        return 0;
    } else {
        return a + produto(a, b - 1);
    }
}

// Função recursiva para calcular a divisão de dois inteiros não negativos
int divisao(int a, int b) {
    if (a < b) {
        return 0;
    } else {
        return 1 + divisao(a - b, b);
    }
}

int main() {
    int num1, num2;

    printf("Digite dois números inteiros não negativos para calcular o produto e a divisão: ");
    scanf("%d %d", &num1, &num2);

    printf("Produto de %d e %d: %d\n", num1, num2, produto(num1, num2));
    printf("Divisão de %d por %d: %d\n", num1, num2, divisao(num1, num2));

    return 0;
}
