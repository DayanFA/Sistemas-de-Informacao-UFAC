/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 01 da Lista 1
Programa.: ufac0001.1
Proposito: Escreva um algoritmo que leia o comprimento de um dos lados de um quadrado, calcule e mostre o perímetro e a sua área.
Ultima atualização: 02/02/2023 Hora: 01:20
*/

#include <stdio.h>
#include <locale.h>

int main (){
    setlocale(LC_ALL, "Portuguese"); //Tive que configura o idioma, pois, os acentos estavam bugando
    int lado;
    printf("Informe o comprimento de um lado do quadrado: ");
    scanf("%d", &lado);
    printf("Perímetro do quadrado: %d\n", 4*lado);
    printf("A área do quadrado: %d\n", lado*lado);
    return 0; // Usarei o return 0 e não o getch, pois já roda no Linux tambem.
}
