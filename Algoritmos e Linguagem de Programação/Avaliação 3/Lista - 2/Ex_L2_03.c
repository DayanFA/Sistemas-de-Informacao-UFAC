/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 03 da Lista 2
Programa.: ufac0002.3
Proposito: Seja um n�mero N natural maior ou igual a 1. Fazer um algoritmo que calcule e mostre o resultado S = 1 + 1/2 +1/3 + 1/4 + ... + 1/N.
Ultima atualiza��o: 08/02/2023 Hora: 01:40
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,n;
    float soma;
    printf("\n\n\n   Entre com um n�mero natural: ");
    scanf("%d", &n);
    soma=0.0;
    for(i=1; i<=n; i++)
    {
        soma=soma+1.0/i; //ou colocar 1/(float)i
    }
    printf("\n\n\n   O resultado do somat�rio �: %f\n\n\n", soma);
    return 0;
}
