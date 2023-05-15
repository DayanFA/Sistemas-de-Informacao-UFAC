/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 04 da Lista 6
Programa.: ufac0006.4
Proposito: Escreva um algoritmo para um programa que, leia uma matriz quadrada 20 por 20 elementos reais.
Depois produza outra matriz, onde cada elemento � obtido dividindo esse elemento pelo elemento da diagonal principal da linha em quest�o.
Em seguida imprima essa matriz na tela do computador.
Ultima atualiza��o: 04/03/2023 Hora: 22:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,j;
    float a[20][20],b[20][20];
    printf("\n\n\n");
    printf("   Entre com a matriz: \n\n\n\n");
    for(i=0; i<20; i++)
    {
        for(j=0; j<20; j++)
        {
            printf("   Entre com o valor da %d� linha da %d� coluna: ", i+1,j+1);
            scanf("%f", &a[i][j]);
            printf("\n");
        }
    }
    for(i=0; i<20; i++)
    {
        for(j=0; j<20; j++)
        {
            b[i][j]=a[i][j]/a[i][i];
        }
    }
    printf("\n\n\n");
    printf("   Aqui esta a matriz dividida pela sua diagonal principal: \n\n\n\n");
    for(i=0; i<20; i++)
    {
        printf("\n");
        for(j=0; j<20; j++)
        {
            printf("   %.2f", b[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");
    return 0;
}
