/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 06 da Lista 5
Programa.: ufac0005.6
Proposito: Fazer um algoritmo que calcule o valor de S, dado por: S = 37x38/1 + 36x37/2 + 35x36/3 + ... + 1x2/37
Ultima atualização: 13/02/2023 Hora: 00:20
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
    for(i=37; i>=1; i--)
    {
        soma=soma+(i*(i+1))/(float)aux;
        aux=aux+1;
    }
    printf("\n\n\n");
    printf("   O valor de S = %f", soma);
    printf("\n\n\n");
    return 0;
}
