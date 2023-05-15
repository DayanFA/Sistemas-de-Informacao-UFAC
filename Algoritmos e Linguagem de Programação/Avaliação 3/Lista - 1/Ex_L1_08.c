/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 08 da Lista 1
Programa.: ufac0001.8
Proposito: Escreva um algoritmo que leia um número natural e mostre se o mesmo é par ou ímpar.
Ultima atualização: 02/02/2023 Hora: 20:50
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int num;
    printf("Informe um número natural: ");
    scanf("%d", &num);
    if(num%2==0){
        printf("O número %d é par.\n", num);
    } else{
        printf("O número %d é Ímpar.\n", num);
    }
    return 0;
}
