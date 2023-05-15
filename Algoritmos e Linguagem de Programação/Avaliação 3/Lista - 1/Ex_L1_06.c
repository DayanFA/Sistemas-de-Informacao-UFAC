/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 06 da Lista 1
Programa.: ufac0001.6
Proposito: Escreva um algoritmo que calcule e mostre a m�dia aritm�tica de n n�meros inteiros quaisquer.
Ultima atualiza��o: 02/02/2023 Hora: 06:50
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int n,soma,i,num;
    float media;
    soma=0;
    printf("Informe a quantidade de n�meros: ");
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        printf("Informe o %d� n�mero: ", i);
        scanf("%d", &num);
        soma=soma+num;
    }
    media=(float)soma/n;
    printf("A m�dia aritm�tica �: %f\n", media); //reduzir as casas decimais s� colocar '%.2f' por exemoplo.
    return 0;
}
