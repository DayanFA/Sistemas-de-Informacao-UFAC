/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 01 da Lista 4
Programa.: ufac0004.1
Proposito: Dadas duas matrizes A e B de ordem 4. Escreva um algoritmo que faça a soma das matrizes, guarde o resultado numa matriz C e mostre o resultado na tela de um computador IBM.
Ultima atualização: 11/02/2023 Hora: 21:50
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[4][4],b[4][4],c[4][4],i,j;
    printf("\n\n\n");
    printf("   Entre com a matriz A: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            printf("   Entre com o valor da %dª linha da %dª coluna: ", i+1,j+1);
            scanf("%d", &a[i][j]);
            printf("\n");
        }
    }
    printf("\n\n\n");
    printf("   Entre com a matriz B: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            printf("   Entre com o valor da %dª linha da %dª coluna: ", i+1,j+1);
            scanf("%d", &b[i][j]);
            printf("\n");
        }
    }
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            c[i][j]=a[i][j]+b[i][j];
        }
    }
    printf("\n\n\n");
    printf("   A soma das matrizes é: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        printf("\n");
        for(j=0; j<4; j++)
        {
            printf("   %d", c[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");
    return 0;
}
