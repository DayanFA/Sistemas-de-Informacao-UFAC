/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 02 da Lista 4
Programa.: ufac0004.2
Proposito: Dada uma matriz A de ordem 4. Escreva um algoritmo que obtenha a matriz transposta da mesma e guarde o resultado em uma matriz AT de ordem 4 também.
Ultima atualização: 11/02/2023 Hora: 22:03
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[4][4],at[4][4],i,j;
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
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            at[i][j]=a[j][i];
        }
    }
    printf("\n\n\n");
    printf("   A matriz transposta de A: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        printf("\n");
        for(j=0; j<4; j++)
        {
            printf("   %d", at[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");
    return 0;
}
