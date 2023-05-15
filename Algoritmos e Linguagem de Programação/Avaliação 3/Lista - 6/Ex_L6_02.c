/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 02 da Lista 6
Programa.: ufac0006.2
Proposito: Dada uma matriz de ordem 4, com n�meros inteiros. Escreva um algoritmo que verifique se a mesma � sim�trica (aij = aji) ou n�o.
Ultima atualiza��o: 04/03/2023 Hora: 15:10
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,j,simetrica,a[4][4];
    printf("\n\n\n");
    printf("   Entre com uma matriz: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            printf("   Entre com o valor da %d� linha da %d� coluna: ", i+1,j+1);
            scanf("%d", &a[i][j]);
            printf("\n");
        }
    }
    simetrica=1;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(a[i][j] != a[j][i])
            {
                simetrica=0;
            }
        }
    }
    if (simetrica==1)
    {
        printf("\n\n\n");
        printf("   � simetrica");
    }
    else
    {
        printf("\n\n\n");
        printf("   N�o � simetrica");
    }
    printf("\n\n\n");
    return 0;
}
