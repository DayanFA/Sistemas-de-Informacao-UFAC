/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 08 da Lista 2
Programa.: ufac0002.8
Proposito: Escreva um algoritmo que mostre em uma tela de computador IBM, os 20 primeiros números primos.
Ultima atualização: 08/02/2023 Hora: 03:12
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,conta,conta_primo,n;
    printf("\n\n\n   Mostrando os 20 primeiros números primos: \n\n\n\n");
    n=2;
    conta_primo=1;
    while(conta_primo<=20)
    {
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
            printf("   %d, ", n);
            conta_primo=conta_primo+1;
        }
        n=n+1;
    }
    printf("\n\n\n");
    return 0;
}
