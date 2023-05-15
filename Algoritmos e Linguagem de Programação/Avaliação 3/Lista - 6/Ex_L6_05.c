/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 05 da Lista 6
Programa.: ufac0006.5
Proposito: Escreva um algoritmo que leia uma matriz A de ordem 4 e verifique se a mesma é uma matriz identidade.
Ultima atualização: 04/03/2023 Hora: 22:30
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[4][4],i,j,identidade;
    printf("\n\n\n");
    printf("   Entre com a matriz: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            printf("   Entre com o valor da %dª linha da %dª coluna: ", i+1,j+1);
            scanf("%d", &a[i][j]);
            printf("\n");
        }
    }
    identidade=1;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(i==j)
            {
                if(a[i][j]!=1)
                {
                    identidade=0;
                }
            }
            else
            {
                if(a[i][j]!=0)
                {
                    identidade=0;
                }
            }
        }
    }
    printf("\n\n\n");
    if(identidade==1)
    {
        printf("   É matriz identidade");
    }
    else
    {
        printf("   Não é matriz identidade");
    }
    printf("\n\n\n");
    return 0;
}
