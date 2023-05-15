/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 04 da Lista 2
Programa.: ufac0002.4
Proposito: A s�rie de Fibonacci � formada pela seq��ncia (1, 1, 2, 3, 5, 8, 13, ... ). Escreva um algoritmo que mostre a s�rie de Fibonacci at� o vig�simo termo.
Ultima atualiza��o: 08/02/2023 Hora: 01:55
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int ant1, ant2,prox,i;
    ant1=1;
    ant2=1;
    printf("\n\n\n   S�rie Fibonacci at� o vig�simo termo: \n\n\n\n");
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
