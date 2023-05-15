/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 02 da Lista 2
Programa.: ufac0002.2
Proposito: Escreva um algoritmo que escreva os n�meros (-1 , 4 , -3 , 8 , -5 , 12, -7) na tela de um computador IBM.
Ultima atualiza��o: 07/02/2023 Hora: 07:45
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i;
    printf("\n\n\n");
    for(i=1; i<=7; i++)
    {
        if(i%2==0)
        {
            printf("   %d ", 2*i);
        }
        else
        {
            printf("   %d ", -i);
        }
    }
    printf("\n\n\n");
    return 0;
}
