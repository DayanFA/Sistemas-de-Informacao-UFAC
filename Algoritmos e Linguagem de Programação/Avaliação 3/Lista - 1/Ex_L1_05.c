/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 05 da Lista 1
Programa.: ufac0001.5
Proposito: Escreva um algoritmo que calcule e mostre o somatório dos números de 1 a 100.
Ultima atualização: 02/02/2023 Hora: 4:00
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int i,soma;
    soma=0;
    for(i=1; i<=100; i++){
        soma=soma+i;
    }
    printf("O Somatório dos números de 1 a 100 é: %d\n", soma);
    return 0;
}
