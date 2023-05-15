/*
Nome do Aluno(a): Dayan Freitas Alves
Disciplina: CCET005 - Algoritmos e Linguagem de Programação
IFES: Universidade Federal do Acre
Exercício 02 da Lista 3
Programa.: ufac0003.2
Proposito: Um comerciante deseja fazer um levantamento de lucros das mercadorias que ele vende. Para isto, mandou digitar uma linha para cada mercadoria com o código, nome, preço de custo e preço de venda das mesmas. Fazer um algoritmo que determine e escreva quantas mercadorias proporcionam:
lucro < 10%
10% < lucro < 20%
lucro > 20%
Ob.: Para finalizar a entrada de dados, deve ser digitado o código igual a zero.
Ultima atualização: 09/02/2023 Hora: 03:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int lucro, lucroma20, lucrome10, lucro10e20, codigo;
    char nome[50];
    float custo, venda;
    lucrome10=0;
    lucroma20=0;
    lucro10e20=0;
    printf("\n\n\n");
    printf("   Informe o código da mercadoria: (Para sair digite 0): ");
    scanf("%d", &codigo);
    while (codigo != 0)
    {
        printf("   Informe o nome da mercadoria: ");
        scanf("%s", nome);
        printf("   Informe o preço de custo da mercadoria: ");
        scanf("%f", &custo);
        printf("   Informe o preço de venda da mercadoria: ");
        scanf("%f", &venda);
        lucro = venda-custo;
        if (lucro < custo*0.1)
        {
            lucrome10 = lucrome10 + 1;
        }
        else
        {
            if (lucro >= custo*0.1 && lucro <= custo*0.2)
            {
                lucro10e20 = lucro10e20 + 1;
            }
            else
            {
                lucroma20=lucroma20 + 1;
            }
        }
        printf("\n\n\n");
        printf("   Informe o código da nova mercadoria: (Para sair digite 0): ");
        scanf("%d", &codigo);
    }
    printf("\n\n\n");
    printf("Quantidade de mercadorias com lucro menor que 10%%: %d", lucrome10);
    printf("\n\n\n");
    printf("Quantidade de mercadorias com lucro entre 10%% e 20%%: %d", lucro10e20);
    printf("\n\n\n");
    printf("Quantidade de mercadorias com lucro maior que 20%%: %d", lucroma20);
    printf("\n\n\n");
    return 0;
}
