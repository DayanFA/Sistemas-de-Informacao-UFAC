/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 06 da Lista 6
Programa.: ufac0006.6
Proposito: Escreva um algoritmo que obtenha a matriz de pascal e depois imprima a mesma na tela do computador.
Obs.: A matriz de pascal de ordem 7 é mostrada abaixo:
P = {1 , 0 , 0 , 0 , 0 , 0 , 0} , {1 , 1 , 0 , 0 , 0 , 0 , 0} , {1 , 2 , 1 , 0 , 0 , 0 , 0} , {1 , 3 , 3 , 1 , 0 , 0 , 0} , {1 , 4 , 6 , 4 , 1 , 0 , 0} , {1 , 5 , 10 , 10 , 5 , 1 , 0} , {1 , 6 , 15 , 20 , 15 , 6 , 1}
Ultima atualização: 04/03/2023 Hora: 23:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,j,p[7][7];
    printf("\n\n\n");
    printf("   Mostrando a matriz de pascal: \n\n\n\n");
    for(i=0; i<7; i++)
    {
        for(j=0; j<7; j++)
        {
            if(i==j || j==0)
            {
                p[i][j]=1;
            }
            else
            {
                if(i>j)
                {
                    p[i][j]=p[i-1][j-1]+p[i-1][j];
                }
                else
                {
                    p[i][j]=0;
                }
            }
        }
    }
    for(i=0; i<7; i++)
    {
        printf("\n");
        for(j=0; j<7; j++)
        {
            printf("   %d", p[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");
    return 0;
}
