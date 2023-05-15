/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 07 da Lista 6
Programa.: ufac0006.7
Proposito: Uma matriz de SkyFall de ordem 4 é definida da seguinte forma:
{0 , 1 , 0 , 1} , {1 , 0 , 1 , 0} , {0 , 1 , 0 , 1} , {1 , 0 , 1 , 0}
Escreva um algoritmo que obtenha
uma matriz do tipo SkyFall de ordem 4 e depois a imprima na tela do computador.
Ultima atualização: 04/03/2023 Hora: 23:20
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int m[4][4],i,j,aux,n;
    printf("\n\n\n");
    printf("   Mostrando a matriz SkyFall: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            n=i+j;
            aux=n%2;
            if(aux==0)
            {
                m[i][j]=0;
            }
            else
            {
                m[i][j]=1;
            }
        }
    }
    for(i=0; i<4; i++)
    {
        printf("\n");
        for(j=0; j<4; j++)
        {
            printf("   %d", m[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");
    return 0;
}
