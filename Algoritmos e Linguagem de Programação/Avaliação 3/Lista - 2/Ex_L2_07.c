/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 07 da Lista 2
Programa.: ufac0002.7
Proposito: Escreva um algoritmo que leia um número natural N (N≥2) e mostre se o mesmo é primo ou não.
Ultima atualização: 08/02/2023 Hora: 02:55
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese"); // por algum motivo o code block muda o encoding para UTF-8 e o portugues não funciona, deixei sem acento mesmo
    int i,n,conta;
    printf("\n\n\n   Entre com um numero natural maior que 1: ");
    scanf("%d", &n);
    conta=0;
    for(i=1; i<=n; i++)
    {
        if(n%i==0)
        {
            conta=conta+1;
        }
    }
    if(conta==2)
    {
        printf("\n\n\n   E primo \n\n\n");
    }
    else
    {
        printf("\n\n\n   Nao e primo \n\n\n");
    }
    return 0;
}
