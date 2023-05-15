/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 01 da Lista 1
Programa.: ufac0001.1
Proposito: Escreva um algoritmo que leia o comprimento de um dos lados de um quadrado, calcule e mostre o per�metro e a sua �rea.
Ultima atualiza��o: 02/02/2023 Hora: 01:20
*/

#include <stdio.h>
#include <locale.h>

int main (){
    setlocale(LC_ALL, "Portuguese"); //Tive que configura o idioma, pois, os acentos estavam bugando
    int lado;
    printf("Informe o comprimento de um lado do quadrado: ");
    scanf("%d", &lado);
    printf("Per�metro do quadrado: %d\n", 4*lado);
    printf("A �rea do quadrado: %d\n", lado*lado);
    return 0; // Usarei o return 0 e n�o o getch, pois j� roda no Linux tambem.
}
