/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 10 da Lista 1
Programa.: ufac0001.10
Proposito: Escreva um algoritmo que leia 3 números naturais, verifique se eles formam um triângulo e mostre a sua classificação.
Ultima atualização: 02/02/2023 Hora: 23:00
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int a,b,c;
    printf("Informe o 1º número natural: ");
    scanf("%d", &a);
    printf("Informe o 2º número natural: ");
    scanf("%d", &b);
    printf("Informe o 3º número natural: ");
    scanf("%d", &c);
    if(a<b+c&&b<a+c&&c<a+b){
        if(a==b&&b==c&&a==c){
            printf("Os lados formam um triângulo equilátero.\n");
        } else{
            if(a==b||b==c||a==c){
                printf("Os lados formam um triângulo isósceles.\n");
            } else{
                printf("Os lados formam um triângulo escaleno.\n");
            }
        }
    }else{
        printf("Os lados não formam um triângulo.\n");
    }
    return 0;
}
