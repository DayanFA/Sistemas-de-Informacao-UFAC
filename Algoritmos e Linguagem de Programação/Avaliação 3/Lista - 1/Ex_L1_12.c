/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 12 da Lista 1
Programa.: ufac0001.12
Proposito: Escreva um algoritmo que calcule e mostre a m�dia aritm�tica dos n�meros pares entre 50 e 100.
Ultima atualiza��o: 03/02/2023 Hora: 01:00
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
    printf("A m�dia dos n�meros pares entre 50 e 100 �: %.2f\n", media);
    return 0;
}
