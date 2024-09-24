/*
Exercícios:
    1) Escreva uma função em C para calcular o fatorial de um número inteiro não negativo.

    int fatorial(int n){
        if(n <= 1)
            return 1;
        else
            return n*fatorial(n-1);
    }

    2) Escreva uma função recursiva em C para calcular o n-ésimo termo da série da serie fibonacci.
    
    int fib(int n){
        if(n <= 2)
            return 1;
        else
            return fib(n-1) + fib(n-2);
    }

    3) Escreva uma função recursiva para:

        a) Calcular o produto de dois números inteiros não negativos.
        b) Calcular a divisão de dois inteiros não negativos.

*/

#include <stdio.h>

//PROTOTIPAÇÃO DAS FUNÇÕES

int fatorial(int n);
int fib(int n);

int main()
{
    int num, fat;
    printf("\nDigite um número não negativo: ")
    scanf("%d", &num);
    fat = fatorial(num);
    printf("\n%d",fat);
    //termo = fib(num);
    //printf("\n%d",termo);
    return 0;
}

int fatorial(int n){
    if(n <= 1)
        return 1;
    else
        return n*fatorial(n-1);
}

int fib(int n){
    if(n <= 2)
        return 1;
    else
        return fib(n-1) + fib(n-2);
}
