/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 09 da Lista 4
Programa.: ufac0004.9
Proposito: Escreva um algoritmo que:
Leia um número n inteiro maior que 0
Leia um vetor de n elementos inteiros
Leia um número x inteiro
Procure no vetor por um elemento que seja igual ao valor de x
1. A busca é feita a partir do primeiro elemento do vetor, até encontrar o elemento, ou até chegar ao fim
do mesmo.
2. Se o elemento for encontrado, obter seu índice
3. Se o elemento não for encontrado, obter –1
Escreva este resultado.
Ultima atualização: 12/02/2023 Hora: 17:20
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int n,x,i,v[1000],achou;
    printf("\n\n\n");
    printf("   Entre com o tamanho do Vetor: ");
    scanf("%d", &n);
    printf("\n\n\n");
    for(i=0; i<n; i++)
    {
        printf("   Entre com o %dº valor: ", i+1);
        scanf("%d", &v[i]);
        printf("\n");
    }
    printf("\n\n\n");
    printf("   Entre com o valor do número desejado: ");
    scanf("%d", &x);
    achou=0;
    i=0;
    printf("\n\n\n");
    while(i<=n && achou==0)
    {
        if(v[i]==x)
        {
            achou=1;
        }
        else
        {
            i=i+1;
        }
    }
    if(achou==1)
    {
        printf("   O número %d foi encontrado no vetor, no indice %d", x,i+1);
    }
    else
    {
        printf("   O número %d não foi encontrado no vetor", x);
    }
    printf("\n\n\n");
    return 0;
}
