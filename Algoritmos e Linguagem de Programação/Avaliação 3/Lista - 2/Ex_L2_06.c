/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programa��o
IFES: Universidade Federal do Acre
Exerc�cio 06 da Lista 2
Programa.: ufac0002.6
Proposito: Escreva um algoritmo que mostre os n�meros (1 , 1/4 , 1/9 , 1/16 , 1/25 , 1/36) na tela de um computador IBM.
Ultima atualiza��o: 08/02/2023 Hora: 02:35
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i;
    i=1;
    printf("\n\n\n");
    printf("   %d, ", i);
    for(i=2; i<=6; i++)
    {
    printf("  1/%d, ", i*i); // j� que a quest�o pede para 'mostar'. Eu poderia tbm usar a biblioteca 'gmp.h' mas, � mais complexa pelo oq eu vi e tem q instalar no code block.
    //ou poderia ser s� printf("%f, ", 1.0/(i*i));
    }
    printf("\n\n\n");
    return 0;
}
