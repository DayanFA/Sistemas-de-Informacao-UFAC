/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 05 da Lista 1
Programa.: ufac0001.5
Proposito: Escreva um algoritmo que calcule e mostre o somat�rio dos n�meros de 1 a 100.
Ultima atualiza��o: 02/02/2023 Hora: 4:00
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
    printf("O Somat�rio dos n�meros de 1 a 100 �: %d\n", soma);
    return 0;
}
