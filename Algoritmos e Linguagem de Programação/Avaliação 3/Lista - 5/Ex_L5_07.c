/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 07 da Lista 5
Programa.: ufac0005.7
Proposito: Fazer um algoritmo que calcule o valor de S, dado por: S = + 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 + ... -10/100
Ultima atualização: 13/02/2023 Hora: 00:30
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,sinal;
    float soma;
    printf("\n\n\n");
    soma=0.0;
    sinal=(+1);
    for(i=1; i<=10; i++)
    {
        soma=soma+sinal*i/(float)(i*i);
        sinal=sinal*(-1);
    }
    printf("\n\n\n");
    printf("   O valor de S = %f", soma);
    printf("\n\n\n");
    return 0;
}
