/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 10 da Lista 4
Programa.: ufac0004.10
Proposito: Escreva um algoritmo que:
Leia um n�mero n inteiro maior que 0 (que pode ser par ou impar)
Leia um vetor de n elementos caracteres
Teste se o vetor � uma palindrome, isto �, se os caracteres lidos do in�cio para o fim ou do fim para o
in�cio, representam a mesma palavra. Para isto ser verdade, o primeiro caractere deve ser igual ao �ltimo
caracter,..., at� chegar-se ao meio do vetor.
Escreva uma mensagem �Sim� ou �N�o�, informando se o vetor � uma palindrome ou n�o. Veja um
exemplo de palindrome:
A N A
Ultima atualiza��o: 12/02/2023 Hora: 17:50
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
        printf("   Entre com a %d� letra: ", i+1);
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
        printf("   Sim, � um palindrome");
    }
    else
    {
        printf("   N�o, n�o � um palindrome");
    }
    printf("\n\n\n");
    return 0;
}
