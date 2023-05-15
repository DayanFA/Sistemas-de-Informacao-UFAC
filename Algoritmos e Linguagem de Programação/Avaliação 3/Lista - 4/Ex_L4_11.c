/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 11 da Lista 4
Programa.: ufac0004.11
Proposito: Escreva um algoritmo que:
Leia dois números m e n inteiros maiores que 0.
Leia uma matriz de m linhas e n colunas, com números inteiros distintos.
Determine:
1. O valor do maior número inteiro da matriz
2. Os índices (linha e coluna) do maior número inteiro.
3. O valor do menor número inteiro da matriz
4. Os índices (linha e coluna) do menor número inteiro da matriz.
Escreva os resultados.
Ultima atualização: 12/02/2023 Hora: 20:30
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int m,n,ma,me,lima,lime,coma,come,a[100][100],i,j; //ia colocar 1000 mas 1000 quebra o computador, se não tiver rodando baixa pra 10
    printf("\n\n\n");
    printf("   Entre com o número de linhas da matriz: ");
    scanf("%d", &m);
    printf("\n\n\n");
    printf("   Entre com o número de colunas da matriz: ");
    scanf("%d", &n);
    printf("\n\n\n");
    for(i=0; i<m; i++)
    {
        for(j=0; j<n; j++)
        {
            printf("   Entre com o valor da %dª linha da %dª coluna: ", i+1,j+1);
            scanf("%d", &a[i][j]);
            printf("\n");
        }
    }
    ma=a[0][0];
    lima=0;
    coma=0;
    me=a[0][0];
    lime=0;
    come=0;
    for(i=0; i<m; i++)
    {
        for(j=0; j<n; j++)
        {
            if(a[i][j]>ma)
            {
                ma=a[i][j];
                lima=i;
                coma=j;
            }
            else
            {
                if(a[i][j]<me)
                {
                    me=a[i][j];
                    lime=i;
                    come=j;
                }
            }
        }
    }
    printf("\n\n\n");
    printf("   O maior valor é %d, na %dª linha da %dª coluna", ma,lima+1,coma+1);
    printf("\n\n");
    printf("   O menor valor é %d, na %dª linha da %dª coluna", me,lime+1,come+1);
    printf("\n\n\n");
    return 0;
}
