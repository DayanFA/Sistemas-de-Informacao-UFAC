/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 02 da Lista 1
Programa.: ufac0001.2
Proposito: Escreva um algoritmo que leia o comprimento da base e da altura de um tri�ngulo, calcule e mostre a �rea do mesmo.
Ultima atualiza��o: 02/02/2023 Hora: 01:30
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int base,altura;
    float area;
    printf("Informe o comprimento da base do tri�ngulo: ");
    scanf("%d", &base);
    printf("Informe o comprimento da altura do tri�ngulo: ");
    scanf("%d", &altura);
    area=(base*altura)/2;
    printf("A �rea do tri�ngulo: %f\n", area);
    return 0;
}
