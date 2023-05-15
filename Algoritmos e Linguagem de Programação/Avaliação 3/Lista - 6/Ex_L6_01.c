/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 01 da Lista 6
Programa.: ufac0006.1
Proposito: Escreva um algoritmo que calcule a soma dos 30 primeiros termos da série: S = 480/10 - 475/11 + 470/12 - 465/13 + ...
Ultima atualização: 04/03/2023 Hora: 15:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,aux1,aux2,sinal;
    float soma;
    soma=0.0;
    sinal=(+1);
    aux1=480;
    aux2=10;
    i=1;
    while(i<=30)
    {
        soma=soma+sinal*(aux1/(float)aux2);
        aux1=aux1-5;
        aux2=aux2+1;
        i=i+1;
        sinal=sinal*(-1);
    }
    printf("\n\n\n");
    printf("   O somatório é: %f", soma);
    printf("\n\n\n");
    return 0;
}
