/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 10 da Lista 4
Programa.: ufac0004.10
Proposito: Escreva um algoritmo que:
Leia um número n inteiro maior que 0 (que pode ser par ou impar)
Leia um vetor de n elementos caracteres
Teste se o vetor é uma palindrome, isto é, se os caracteres lidos do início para o fim ou do fim para o
início, representam a mesma palavra. Para isto ser verdade, o primeiro caractere deve ser igual ao último
caracter,..., até chegar-se ao meio do vetor.
Escreva uma mensagem “Sim” ou “Não”, informando se o vetor é uma palindrome ou não. Veja um
exemplo de palindrome:
A N A
Ultima atualização: 12/02/2023 Hora: 17:50
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i,n,p;
    char v[1000];
    printf("\n\n\n");
    printf("   Entre com o tamanho do Vetor: ");
    scanf("%d", &n);
    printf("\n\n\n");
    for(i=0; i<n; i++)
    {
        printf("   Entre com a %dº letra: ", i+1);
        scanf("%s", &v[i]);
        printf("\n");
    }
    p=1;
    i=0;
    printf("\n\n\n");
    while(i<=n && p==1)
    {
        if(v[i]!=v[n-i-1])
        {
            p=0;
        }
            i=i+1;
    }
    if(p==1)
    {
        printf("   Sim, é um palindrome");
    }
    else
    {
        printf("   Não, não é um palindrome");
    }
    printf("\n\n\n");
    return 0;
}
