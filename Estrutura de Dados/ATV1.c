/*
O método de ordenação da bolha é um algoritmo simples que percorre a lista de itens a serem ordenados várias vezes. 
Em cada iteração, ele compara os elementos adjacentes e os troca de posição se estiverem na ordem errada. 
O processo é repetido até que nenhuma troca seja necessária, indicando que a lista está ordenada. 
A complexidade do algoritmo da bolha é O(n^2), onde 'n' é o número de elementos a serem ordenados. 
Isso ocorre porque, no pior caso, o algoritmo precisa percorrer a lista várias vezes.
*/

#include <stdio.h>

// Função para ordenar o vetor movendo o menor elemento para o inícior; Essa é mais direta como da de ver
void ordenacaoBolhaComMenorInicio(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = tamanho - 1; j > i; j--) {
            if (vetor[j] < vetor[j - 1]) {
                int temp = vetor[j];
                vetor[j] = vetor[j - 1];
                vetor[j - 1] = temp;
            }
        }
    }
}

// Função para ordenar o vetor movendo o menor para o início e o maior para o final; Essa requer mais manipulações 
// e verificações adicionais durante o processo de ordenação.
void ordenacaoBolhaComMenorInicioMaiorFim(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho / 2; i++) {
        for (int j = i; j < tamanho - i - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                int temp = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = temp;
            }
            if (vetor[tamanho - 1 - j] < vetor[tamanho - 2 - j]) {
                int temp = vetor[tamanho - 1 - j];
                vetor[tamanho - 1 - j] = vetor[tamanho - 2 - j];
                vetor[tamanho - 2 - j] = temp;
            }
        }
    }
}

void imprimirVetor(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main() {
    int vetor[] = {55, 43, 645, 4, 6, 11, 20};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor original: \n");
    imprimirVetor(vetor, tamanho);

    // Aplicar a ordenação levando o menor elemento para o início
    ordenacaoBolhaComMenorInicio(vetor, tamanho);
    printf("Vetor ordenado com o menor no início: \n");
    imprimirVetor(vetor, tamanho);

    // Aplicar a ordenação levando o menor para o início e o maior para o final
    ordenacaoBolhaComMenorInicioMaiorFim(vetor, tamanho);
    printf("Vetor ordenado com o menor no início e o maior no final: \n");
    imprimirVetor(vetor, tamanho);

    return 0;
}


/*
A complexidade do método de ordenação da variação: 
a) é a mesma que a função bolha padrão, ou seja, O(n^2). 
b) é também O(n^2) no pior caso, mas pode ser mais eficiente do que o 
algoritmo de bolha padrão em certas situações.
*/


