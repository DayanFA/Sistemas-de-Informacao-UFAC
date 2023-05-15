/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 06 da Lista 1
Programa.: ufac0001.6
Proposito: Escreva um algoritmo que calcule e mostre a média aritmética de n números inteiros quaisquer.
Ultima atualização: 02/02/2023 Hora: 06:50
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int n,soma,i,num;
    float media;
    soma=0;
    printf("Informe a quantidade de números: ");
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        printf("Informe o %dº número: ", i);
        scanf("%d", &num);
        soma=soma+num;
    }
    media=(float)soma/n;
    printf("A média aritmética é: %f\n", media); //reduzir as casas decimais só colocar '%.2f' por exemoplo.
    return 0;
}
