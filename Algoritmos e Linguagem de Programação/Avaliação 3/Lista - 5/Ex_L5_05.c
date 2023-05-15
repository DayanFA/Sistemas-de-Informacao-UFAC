/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 05 da Lista 5
Programa.: ufac0005.5
Proposito: Fazer um algoritmo que calcule o valor de S, dado por: S = 2^1/50 + 2^2/49 + 2^3/48 + 2^4/47 + ... + 2^50/1
Ultima atualização: 13/02/2023 Hora: 00:10
*/

#include <stdio.h>
#include <math.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int aux,i;
    float soma;
    printf("\n\n\n");
    soma=0.0;
    aux=1;
    for(i=50; i>=1; i--)
    {
        soma=soma+(pow(2,aux)/(float)i);
        aux=aux+1;
    }
    printf("\n\n\n");
    printf("   O valor de S = %f", soma);
    printf("\n\n\n");
    return 0;
}
