/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 03 da Lista 1
Programa.: ufac0001.3
Proposito: Escreva um algoritmo que leia os coeficientes de uma equação do 2º grau, e se possível, encontre e mostre sua solução.
Ultima atualização: 02/02/2023 Hora: 02:00
*/

#include <stdio.h>
#include <math.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int a,b,c,delta;
    float x1,x2;
    printf("Informe o coeficiente a: ");
    scanf("%d", &a);
    printf("Informe o coeficiente b: ");
    scanf("%d", &b);
    printf("Informe o coeficiente c: ");
    scanf("%d", &c);
    delta=(b*b)-(4*a*c); //pode usar o pow(b,2) para número elevado
    if(delta>0){
        x1=(-b+sqrt(delta))/(2*a);
        x2=(-b-sqrt(delta))/(2*a);
        printf("As soluções são:\n");
        printf("x1 = %f\n", x1);
        printf("x2 = %f\n", x2);
    } else {
        if(delta==0){
            x1 = -b/(2*a);
            printf("A solução é: %f\n", x1);
        } else{
            printf("Não existe solução real");
        }
    }
    return 0;
}
