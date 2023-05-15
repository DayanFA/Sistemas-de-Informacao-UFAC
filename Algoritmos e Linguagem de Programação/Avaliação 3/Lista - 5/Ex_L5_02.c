/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 02 da Lista 5
Programa.: ufac0005.2
Proposito: Dado o vetor V de caracteres abaixo:
 ! U O T R E C A
Qual será a configuração depois de executados os comandos?
Para I =1 até 4 passo 1
AUX ← V[I]
V[I] ← V[8 – I +1 ]
V[ 8 – I + 1 ] ← AUX
Fim_Para
Ultima atualização: 12/02/2023 Hora: 23:30
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i;
    char aux;
    char v[8]= {'!', 'U', 'O', 'T', 'R', 'E', 'C', 'A'}; //declarando o vetor
    printf("\n\n\n");
    for(i=0; i<4; i++)
    {
        aux=v[i];
        v[i]=v[8-i-1];
        v[8-i-1]=aux;
    }
    printf("   A configuracao resultante sera:");
    for(i=0; i<8; i++)
    {
        printf(" %c", v[i]);
    }
    printf("\n\n\n");
    return 0;
}
