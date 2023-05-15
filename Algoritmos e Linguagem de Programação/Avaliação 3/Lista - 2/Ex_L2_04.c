/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 04 da Lista 2
Programa.: ufac0002.4
Proposito: A série de Fibonacci é formada pela seqüência (1, 1, 2, 3, 5, 8, 13, ... ). Escreva um algoritmo que mostre a série de Fibonacci até o vigésimo termo.
Ultima atualização: 08/02/2023 Hora: 01:55
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int ant1, ant2,prox,i;
    ant1=1;
    ant2=1;
    printf("\n\n\n   Série Fibonacci até o vigésimo termo: \n\n\n\n");
    printf("   %d,  %d, ", ant1, ant2);
    for(i=1; i<=18; i++)
    {
        prox=ant1+ant2;
        printf(" %d, ", prox);
        ant1=ant2;
        ant2=prox;
    }
    printf("\n\n\n");
    return 0;
}
