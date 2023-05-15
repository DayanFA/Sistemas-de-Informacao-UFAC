/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 09 da Lista 1
Programa.: ufac0001.9
Proposito: Escreva um algoritmo que leia 10 n�meros inteiros, calcule e mostre:
a) quantos n�meros s�o menores que 10
b) quantos s�o maiores que 10 e menores que 20
c) quantos s�o maiores que 20.
Ultima atualiza��o: 02/02/2023 Hora: 21:00
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int c1,c2,c3,num,i;
    printf("Entre com 10 n�meros inteiros: \n\n");
    c1=0;
    c2=0;
    c3=0;
    for(i=1; i<=10; i++){
        printf("Informe o %d� n�mero: ", i);
        scanf("%d", &num);
        if(num<10){
            c1=c1+1;
        } else{
            if(num>10&&num<20){
                c2=c2+1;
            } else{
                if(num>20){
                    c3=c3+1;
                }
            }
        }
    }
    printf("O total de n�meros menores que 10: %d\n", c1);
    printf("O total de n�meros maiores que 10 e menores que 20: %d\n", c2);
    printf("O total de n�meros maiores que 20: %d\n", c3);
    return 0;
}
