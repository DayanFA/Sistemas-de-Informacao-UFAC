/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 09 da Lista 6
Programa.: ufac0006.9
Proposito: Escreva um algoritmo calcule a quantidade de números primos em um vetor A. O usuário deve fornece o vetor de 20 números naturais maiores que 1 via teclado.
Ultima atualização: 04/03/2023 Hora: 23:50
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a[20],i,j,cp,aux1,aux2,c;
    printf("\n\n\n");
    printf("   Entre com o vetor, com números maiores que 1: \n\n\n\n");
    for(i=0; i<20; i++)
    {
        printf("   Entre com o %dº valor: ", i+1);
        scanf("%d", &a[i]);
        printf("\n");
    }
    cp=0;
    for(i=0; i<20; i++)
    {
        c=0;
        aux1=a[i];
        for(j=1; j<=aux1; j++)
        {
            aux2=aux1%j;
            if(aux2==0)
            {
                c=c+1;
            }
        }
        if(c==2)
        {
            cp=cp+1;
        }
    }
    printf("\n\n\n");
    printf("   O número de números primos no vetor é: %d", cp);
    printf("\n\n\n");
    return 0;
}
