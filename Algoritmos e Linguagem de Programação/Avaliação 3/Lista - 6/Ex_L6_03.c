/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 03 da Lista 6
Programa.: ufac0006.3
Proposito: Escreva um algoritmo que leia um vetor A com 20 números inteiros, calcule e imprima o valor de S, onde: S ← (A1 - A20)^2 + (A2 - A19)^2 + (A3 - A18)^2 + ... + (A10 - A11)^2
Ultima atualização: 04/03/2023 Hora: 15:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,a[20];
    float soma;
    printf("\n\n\n");
    printf("   Entre com um vetor de 20 numeros naturais: \n\n\n\n");
    for(i=0; i<20; i++)
    {
        printf("   Entre com o %d valor: ", i+1);
        scanf("%d", &a[i]);
        printf("\n");
    }
    soma=0.0;
    for(i=0; i<10; i++)
    {
        soma=soma+((a[i]-a[19-i])*(a[i]-a[19-i]));
    }
    printf("\n\n\n");
    printf("   O somatorio e: %.2f", soma);
    printf("\n\n\n");
    return 0;
}
