/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 07 da Lista 1
Programa.: ufac0001.7
Proposito: Escreva um algoritmo que leia 10 n�meros inteiros, encontre e mostre o menor e o maior deles.
Ultima atualiza��o: 02/02/2023 Hora: 08:30
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int i,num,menor,maior;
    printf("Entre com o 1� n�mero: ");
    scanf("%d", &num);
    maior=num;
    menor=num;
    for(i=2; i<=10; i++){
        printf("Entre com o %d� n�mero: ", i);
        scanf("%d", &num);
        if(num>maior){
            maior=num;
        } else {
            if(num<menor){
                menor=num;
            }
        }
    }
    printf("O maior n�mero �: %d\n", maior);
    printf("O menor n�mero �: %d\n", menor);
    return 0;
}

