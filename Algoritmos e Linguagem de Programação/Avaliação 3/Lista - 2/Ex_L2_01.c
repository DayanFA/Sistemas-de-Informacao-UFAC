/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 01 da Lista 2
Programa.: ufac0002.1
Proposito: Escreva um algoritmo que escreva os números (1 , 4 , 9 , 16 , 25 , 36) na tela de um computador IBM.
Ultima atualização: 07/02/2023 Hora: 07:30
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i;
    printf("\n\n\n");
    for(i=1; i<=6; i++)
    {
        printf("   %d ", i*i);
    }
    printf("\n\n\n");
    return 0;
}
