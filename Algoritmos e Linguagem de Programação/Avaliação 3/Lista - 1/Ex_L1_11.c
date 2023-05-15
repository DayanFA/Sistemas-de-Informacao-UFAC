/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 11 da Lista 1
Programa.: ufac0001.11
Proposito: Escreva um algoritmo que leia 3 n�meros naturais e verifique se eles formam um tri�ngulo ret�ngulo.
Ultima atualiza��o: 02/02/2023 Hora: 23:50
*/

#include <stdio.h>
#include <math.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int a,b,c;
    printf("Informe o 1� n�mero natural: ");
    scanf("%d", &a);
    printf("Informe o 2� n�mero natural: ");
    scanf("%d", &b);
    printf("Informe o 3� n�mero natural: ");
    scanf("%d", &c);
    if(a<b+c&&b<a+c&&c<a+b){
        if(pow(a,2)==pow(b,2)+pow(c,2)||pow(b,2)==pow(a,2)+pow(c,2)||pow(c,2)==pow(a,2)+pow(b,2)){
            printf("Os lados formam um tri�ngulo ret�ngulo.\n");
        } else{
            printf("Os lados n�o formam um tri�ngulo ret�ngulo.\n");
        }
    }else{
        printf("Os lados n�o formam um tri�ngulo.\n");
    }
    return 0;
}
