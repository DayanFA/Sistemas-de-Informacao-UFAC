/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 03 da Lista 1
Programa.: ufac0001.3
Proposito: Escreva um algoritmo que leia os coeficientes de uma equa��o do 2� grau, e se poss�vel, encontre e mostre sua solu��o.
Ultima atualiza��o: 02/02/2023 Hora: 02:00
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
    delta=(b*b)-(4*a*c); //pode usar o pow(b,2) para n�mero elevado
    if(delta>0){
        x1=(-b+sqrt(delta))/(2*a);
        x2=(-b-sqrt(delta))/(2*a);
        printf("As solu��es s�o:\n");
        printf("x1 = %f\n", x1);
        printf("x2 = %f\n", x2);
    } else {
        if(delta==0){
            x1 = -b/(2*a);
            printf("A solu��o �: %f\n", x1);
        } else{
            printf("N�o existe solu��o real");
        }
    }
    return 0;
}
