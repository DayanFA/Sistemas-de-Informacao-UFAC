/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 08 da Lista 1
Programa.: ufac0001.8
Proposito: Escreva um algoritmo que leia um n�mero natural e mostre se o mesmo � par ou �mpar.
Ultima atualiza��o: 02/02/2023 Hora: 20:50
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int num;
    printf("Informe um n�mero natural: ");
    scanf("%d", &num);
    if(num%2==0){
        printf("O n�mero %d � par.\n", num);
    } else{
        printf("O n�mero %d � �mpar.\n", num);
    }
    return 0;
}
