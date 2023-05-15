/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 08 da Lista 5
Programa.: ufac0005.8
Proposito: Escreva um algoritmo que calcule a soma dos 50 primeiros termos da série:  S = - 1000/1 + 997/2 - 994/3 + 991/4 - ...
Ultima atualização: 13/02/2023 Hora: 00:40
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int aux,i,sinal;
    float soma;
    printf("\n\n\n");
    soma=0.0;
    aux=1000;
    sinal=(-1);
    for(i=1; i<=50; i++)
    {
        soma=soma+sinal*(aux/(float)i);
        aux=aux-3;
        sinal=sinal*(-1);
    }
    printf("\n\n\n");
    printf("   O valor de S = %f", soma);
    printf("\n\n\n");
    return 0;
}
