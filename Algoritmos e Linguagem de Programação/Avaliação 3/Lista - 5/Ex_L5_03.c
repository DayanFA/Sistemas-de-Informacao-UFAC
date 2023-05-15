/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 03 da Lista 5
Programa.: ufac0005.3
Proposito: Dado um número N natural maior que zero. Fazer um algoritmo para calcular o valor de s, dado por: S= 1/N + 2/N-1 + 3/N-2 + ... + N-1/2 + N/1
Ultima atualização: 12/02/2023 Hora: 23:40
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int aux,i,n;
    float soma;
    printf("\n\n\n");
    printf("   Entre com o N: ");
    scanf("%d", &n);
    soma=0.0;
    aux=1;
    for(i=n; i>=1; i--)
    {
        soma=soma+(aux/(float)i);
        aux=aux+1;
    }
    printf("\n\n\n");
    printf("   O valor de S = %f", soma);
    printf("\n\n\n");
    return 0;
}
