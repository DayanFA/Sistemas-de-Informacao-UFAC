/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 04 da Lista 1
Programa.: ufac0001.4
Proposito: Escreva um algoritmo que leia dois n�meros distintos, encontre e mostre o maior deles.
Ultima atualiza��o: 02/02/2023 Hora: 03:30
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int a,b;
    printf("Entre com dois n�meros inteiros distintos: \n\n");
    printf("Informe o primeiro n�mero: ");
    scanf("%d", &a);
    printf("Informe o segundo n�mero: ");
    scanf("%d", &b);
    if(a>b){
        printf("O maior n�mero �: %d\n", a);
    } else{
        if(a==b){
            printf("Os dois n�meros digitados n�o s�o distintos");
        } else{
            printf("O maior n�mero �: %d\n", b);
        }
    }
    return 0;
}
