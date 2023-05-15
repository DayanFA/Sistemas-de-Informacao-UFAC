/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 01 da Lista 5
Programa.: ufac0005.1
Proposito: O valor aproximado do numero π pode ser calculado usando-se a série S = 1 - 1/3^3 + 1/5^3- 1/7^3 + 1/9^3-... sendo π =³√S x 32.
Faça um algoritmo que calcule e imprima o valor de π usando os 51 primeiros termos da série acima.
Ultima atualização: 12/02/2023 Hora: 22:30
*/

#include <stdio.h>
#include <math.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,deno,sinal;
    float soma,pi;
    printf("\n\n\n");
    printf("   Calculo do valor PI:");
    printf("\n\n\n");
    deno=1;
    sinal=(+1);
    soma=0.0;
    for(i=1; i<=51; i++)
    {
        soma=soma+sinal*(1/(float)(deno*deno*deno));
        deno=deno+2;
        sinal=sinal*(-1);
    }
    pi=cbrt(32*soma); //cbrt é a raiz cubica
    printf("   O valor de PI e: %f", pi);
    printf("\n\n\n");
    return 0;
}
