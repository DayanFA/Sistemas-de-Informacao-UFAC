/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 07 da Lista 1
Programa.: ufac0001.7
Proposito: Escreva um algoritmo que leia 10 números inteiros, encontre e mostre o menor e o maior deles.
Ultima atualização: 02/02/2023 Hora: 08:30
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int i,num,menor,maior;
    printf("Entre com o 1º número: ");
    scanf("%d", &num);
    maior=num;
    menor=num;
    for(i=2; i<=10; i++){
        printf("Entre com o %dº número: ", i);
        scanf("%d", &num);
        if(num>maior){
            maior=num;
        } else {
            if(num<menor){
                menor=num;
            }
        }
    }
    printf("O maior número é: %d\n", maior);
    printf("O menor número é: %d\n", menor);
    return 0;
}

