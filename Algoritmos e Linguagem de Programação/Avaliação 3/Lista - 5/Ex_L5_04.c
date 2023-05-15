/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 04 da Lista 5
Programa.: ufac0005.4
Proposito: Fazer um algoritmo que calcule o valor de S, dado por:  S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
Ultima atualização: 12/02/2023 Hora: 23:50
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int aux,i;
    float soma;
    printf("\n\n\n");
    soma=0.0;
    aux=1;
    for(i=1; i<=50; i++)
    {
        soma=soma+(aux/(float)i);
        aux=aux+2;
    }
    printf("\n\n\n");
    printf("   O valor de S = %f", soma);
    printf("\n\n\n");
    return 0;
}
