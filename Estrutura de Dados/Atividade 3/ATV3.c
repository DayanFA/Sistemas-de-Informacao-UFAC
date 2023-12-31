#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No* prox;
    struct No* ant;
} No;

void inserirFim(No** inicio, int valor) {
    if (*inicio == NULL) {
        No* novoNo = (No*)malloc(sizeof(No));
        novoNo->dado = valor;
        novoNo->prox = novoNo->ant = novoNo;
        *inicio = novoNo;
        return;
    }

    No *ultimo = (*inicio)->ant;

    No* novoNo = (No*)malloc(sizeof(No));
    novoNo->dado = valor;

    novoNo->prox = *inicio;

    (*inicio)->ant = novoNo;

    novoNo->ant = ultimo;

    ultimo->prox = novoNo;
}

void exibir(No* inicio) {
    No* temp = inicio;

    while (temp->prox != inicio) {
        printf("%d ", temp->dado);
        temp = temp->prox;
    }
    printf("%d ", temp->dado);
}

int main() {
    No* inicio = NULL;

    inserirFim(&inicio, 5);
    inserirFim(&inicio, 4);
    inserirFim(&inicio, 7);
    inserirFim(&inicio, 8);

    printf("Lista circular duplamente encadeada criada: ");
    exibir(inicio);

    return 0;
}