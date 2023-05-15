/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 04 da Lista 4
Programa.: ufac0004.4
Proposito: Escreva um algoritmo que multiplique um vetor linha V por uma matriz A de ordem n = 4. Mostre o resultado.
Ultima atualização: 11/02/2023 Hora: 23:10
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[4][4],v[4],i,j,soma,r[4];
    printf("\n\n\n");
    printf("   Entre com o Vetor V: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        printf("   Entre com o %dº valor: ", i+1);
        scanf("%d", &v[i]);
        printf("\n");
    }
    printf("\n\n\n");
    printf("   Entre com a matriz A: \n\n\n\n");
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
        soma=0;
        for(j=0; j<4; j++)
        {
            soma=soma+v[j]*a[j][i];
        }
        r[i]=soma;
    }
    printf("\n\n\n");
    printf("   O vetor resultante é: \n\n\n\n");
    for(i=0; i<4; i++)
    {
        printf("   %d ", r[i]);
    }
    printf("\n\n\n");
    return 0;
}
