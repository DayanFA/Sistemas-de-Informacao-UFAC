/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 12 da Lista 1
Programa.: ufac0001.12
Proposito: Escreva um algoritmo que calcule e mostre a média aritmética dos números pares entre 50 e 100.
Ultima atualização: 03/02/2023 Hora: 01:00
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int i,soma,conta;
    float media;
    conta=0;
    soma=0;
    for(i=52; i<=98; i+=2 ){
        soma=soma+i;
        conta=conta+1;
    }
    media=(float)soma/conta;
    printf("A média dos números pares entre 50 e 100 é: %.2f\n", media);
    return 0;
}
