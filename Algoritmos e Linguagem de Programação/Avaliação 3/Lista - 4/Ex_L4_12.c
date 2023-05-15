/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 12 da Lista 4
Programa.: ufac0004.12
Proposito: Escreva um algoritmo que:
Leia um n�mero n inteiro maior que 0
Leia uma matriz de n linhas e n colunas, com elementos reais.
Some todos os elementos da matriz abaixo da diagonal principal
Escreva este resultado.
Ultima atualiza��o: 12/02/2023 Hora: 21:10
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int n,i,j;
    float a[100][100],soma;
    printf("\n\n\n");
    printf("   Entre com o tamanho da matriz: ");
    scanf("%d", &n);
    printf("\n\n\n");
    printf("   Entre com a matriz: \n\n\n\n");
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            printf("   Entre com o valor da %d� linha da %d� coluna: ", i+1,j+1);
            scanf("%f", &a[i][j]);
            printf("\n");
        }
    }
    soma=0.0;
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            if(i>j)
            {
                soma=soma+a[i][j];
            }
        }
    }
    printf("\n\n\n");
    printf("   A soma dos elementos abaixo da diagonal principal �: %f", soma);
    printf("\n\n\n");
    return 0;
}
