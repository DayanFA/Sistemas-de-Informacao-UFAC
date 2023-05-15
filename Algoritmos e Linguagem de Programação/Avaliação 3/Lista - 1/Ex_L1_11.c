/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 11 da Lista 1
Programa.: ufac0001.11
Proposito: Escreva um algoritmo que leia 3 números naturais e verifique se eles formam um triângulo retângulo.
Ultima atualização: 02/02/2023 Hora: 23:50
*/

#include <stdio.h>
#include <math.h>
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
        if(pow(a,2)==pow(b,2)+pow(c,2)||pow(b,2)==pow(a,2)+pow(c,2)||pow(c,2)==pow(a,2)+pow(b,2)){
            printf("Os lados formam um triângulo retângulo.\n");
        } else{
            printf("Os lados não formam um triângulo retângulo.\n");
        }
    }else{
        printf("Os lados não formam um triângulo.\n");
    }
    return 0;
}
