/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 07 da Lista 4
Programa.: ufac0004.7
Proposito: Escreva um algoritmo que calcule e mostre a soma dos elementos da diagonal secundária de uma matriz A quadrada de ordem 4.
Ultima atualização: 12/02/2023 Hora: 16:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[4][4],i,j,soma;
    printf("\n\n\n");
    soma=0;
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
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(i+j==3)
            {
                soma=soma+a[i][j];
            }
        }
    }
    printf("\n\n\n");
    printf("   O traço secundário da matriz é: %d", soma);
    printf("\n\n\n");
    return 0;
}
