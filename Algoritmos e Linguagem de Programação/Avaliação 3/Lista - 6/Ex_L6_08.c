/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 08 da Lista 6
Programa.: ufac0006.8
Proposito: Uma matriz de SkyFall de ordem 4 é definida da seguinte forma:
{0 , 1 , 0 , 1} , {1 , 0 , 1 , 0} , {0 , 1 , 0 , 1} , {1 , 0 , 1 , 0}
Dada uma matriz qualquer de ordem 4, escreva um algoritmo que verifique se a mesma é do tipo SkyFall.
Ultima atualização: 04/03/2023 Hora: 23:40
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int m[4][4],i,j,h,n,aux;
    printf("\n\n\n");
    printf("   Entre com a matriz: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            printf("   Entre com o valor da %dª linha da %dª coluna: ", i+1,j+1);
            scanf("%d", &m[i][j]);
            printf("\n");
        }
    }
    h=1;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            n=i+j;
            aux=n%2;
            if(aux==0)
            {
                if(m[i][j]!=0)
                {
                    h=0;
                }
            }
            else
            {
                if(m[i][j]!=1)
                {
                    h=0;
                }
            }
        }
    }
    printf("\n\n\n");
    if(h==1)
    {
        printf("   É SkyFall");
    }
    else
    {
        printf("   Não é SkyFall");
    }
    printf("\n\n\n");
    return 0;
}
