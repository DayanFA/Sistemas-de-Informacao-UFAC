/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 05 da Lista 4
Programa.: ufac0004.5
Proposito: Escreva um algoritmo que gere uma matriz A de n�meros pares, de ordem 4.
Ultima atualiza��o: 11/02/2023 Hora: 23:25
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[4][4],i,j,num;
    printf("\n\n\n");
    printf("   Matriz de n�meros pares: \n\n\n\n");
    num=0;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            a[i][j]=num;
            num=num+2;
        }
    }
    printf("\n\n\n");
    for(i=0; i<4; i++)
    {
        printf("\n");
        for(j=0; j<4; j++)
        {
            printf("   %d", a[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");
    return 0;
}
