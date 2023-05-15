/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 08 da Lista 4
Programa.: ufac0004.8
Proposito: Dado um vetor V com 20 elementos inteiros fornecidos pelo usu�rio. Escreva um algoritmo que encontre e mostre o maior n�mero inteiro contido no mesmo.
Ultima atualiza��o: 12/02/2023 Hora: 16:30
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int v[20],i,maior;
    printf("\n\n\n");
    printf("   Entre com o Vetor: \n\n\n\n");
    for(i=0; i<20; i++)
    {
        printf("   Entre com o %d� valor: ", i+1);
        scanf("%d", &v[i]);
        printf("\n");
    }
    maior=v[0];
    for(i=1; i<20; i++)
    {
        if(v[i]>maior)
        {
            maior=v[i];
        }
    }
    printf("\n\n\n");
    printf("   O maior n�mero no ventor �: %d\n\n\n\n", maior);
    printf("\n\n\n");
    return 0;
}
