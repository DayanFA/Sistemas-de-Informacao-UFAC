/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 04 da Lista 1
Programa.: ufac0001.4
Proposito: Escreva um algoritmo que leia dois números distintos, encontre e mostre o maior deles.
Ultima atualização: 02/02/2023 Hora: 03:30
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int a,b;
    printf("Entre com dois números inteiros distintos: \n\n");
    printf("Informe o primeiro número: ");
    scanf("%d", &a);
    printf("Informe o segundo número: ");
    scanf("%d", &b);
    if(a>b){
        printf("O maior número é: %d\n", a);
    } else{
        if(a==b){
            printf("Os dois números digitados não são distintos");
        } else{
            printf("O maior número é: %d\n", b);
        }
    }
    return 0;
}
