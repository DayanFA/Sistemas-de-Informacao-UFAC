/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 02 da Lista 1
Programa.: ufac0001.2
Proposito: Escreva um algoritmo que leia o comprimento da base e da altura de um triângulo, calcule e mostre a área do mesmo.
Ultima atualização: 02/02/2023 Hora: 01:30
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int base,altura;
    float area;
    printf("Informe o comprimento da base do triângulo: ");
    scanf("%d", &base);
    printf("Informe o comprimento da altura do triângulo: ");
    scanf("%d", &altura);
    area=(base*altura)/2;
    printf("A área do triângulo: %f\n", area);
    return 0;
}
