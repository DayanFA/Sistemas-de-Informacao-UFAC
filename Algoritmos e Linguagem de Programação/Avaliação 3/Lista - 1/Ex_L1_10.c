/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 10 da Lista 1
Programa.: ufac0001.10
Proposito: Escreva um algoritmo que leia 3 n�meros naturais, verifique se eles formam um tri�ngulo e mostre a sua classifica��o.
Ultima atualiza��o: 02/02/2023 Hora: 23:00
*/

#include <stdio.h>
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
        if(a==b&&b==c&&a==c){
            printf("Os lados formam um tri�ngulo equil�tero.\n");
        } else{
            if(a==b||b==c||a==c){
                printf("Os lados formam um tri�ngulo is�sceles.\n");
            } else{
                printf("Os lados formam um tri�ngulo escaleno.\n");
            }
        }
    }else{
        printf("Os lados n�o formam um tri�ngulo.\n");
    }
    return 0;
}
