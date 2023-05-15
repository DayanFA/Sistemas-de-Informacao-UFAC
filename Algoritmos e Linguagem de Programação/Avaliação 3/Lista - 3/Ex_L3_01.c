/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 01 da Lista 3
Programa.: ufac0003.1
Proposito: Escreva um algoritmo que leia as coordenadas cartesianas de dois pontos do plano, calcule e mostre a distância euclidiana entre esses dois pontos.
Ultima atualização: 09/02/2023 Hora: 01:00
*/

#include <stdio.h>
#include <locale.h>
#include <math.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a1, a2, b1, b2;
    float dist;
    printf("\n\n\n");
    printf("   Informe as coordenadas do primeiro ponto: ");
    scanf("%d %d", &a1, &b1);
    printf("   Informe as coordenadas do segundo ponto: ");
    scanf("%d %d", &a2, &b2);
    dist = sqrt(pow((a2 - a1), 2) + pow((b2 - b1), 2));
    printf("   A distância euclidiana entre os pontos (%d,%d) e (%d,%d) é: %f\n", a1, b1, a2, b2, dist);
    printf("\n\n\n");
    return 0;
}
