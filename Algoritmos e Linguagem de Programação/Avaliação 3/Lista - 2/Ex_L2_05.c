/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 05 da Lista 2
Programa.: ufac0002.5
Proposito: Escreva um algoritmo que leia um numero natural N (N≥1). Calcule e mostre o resultado S = 1 + 1/4 +1/9 + 1/16 + ... + 1/N^2.
Ultima atualização: 08/02/2023 Hora: 02:10
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese"); // por algum motivo o code block muda o encoding para UTF-8 e o portugues não funciona, deixei sem acento mesmo
    int i,n;
    float soma;
    printf("\n\n\n   Entre com um numero natural maior ou igual a 1: ");
    scanf("%d", &n);
    soma=0.0;
    for(i=1; i<=n; i++)
    {
        soma=soma+1.0/(i*i);
    }
    printf("\n\n\n   O somatorio e: %f\n\n\n", soma);
    return 0;
}

