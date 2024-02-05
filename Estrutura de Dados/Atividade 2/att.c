#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

// // Função auxiliar para trocar dois elementos (swap)
// void swap(int *a, int *b) {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

/*
 > Um algoritmo de ordenação é considerado estável quando consegue 
 preservar a ordem de registro de chaves iguais, em outras palavras 
 se os registros aparecem na sequencia ordenada na mesma ordem em que 
 estão na sequencia inicial.
 > Array = Vetor
*/

/*  Bubble Sort ou Ordenação por bolha
 - Compara pares de elementos adjacentes e troca-os se estiverem fora de ordem.
   Repete até que a lista esteja ordenada. Elementos maiores "borbulham" para o final.
 - Estável
 - Versão recursiva é mais lenta que a versão iterativa
 - Ineficiente para arrays grandes

    Complexibilidade
 - Melhor caso: O(N)
 - Caso médio: O(N^2)
 - Pior caso: O(N^2)
*/


// Método de ordenação: Bubble Sort
// Pseudocódigo:
// Função BubbleSort(lista):
//     n = comprimento da lista
//     para i de 0 até n-1, exclusivo:
//         para j de 0 até n-i-1, exclusivo:
//             se lista[j] > lista[j+1]:
//                 trocar lista[j] e lista[j+1]

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // swap(&arr[j], &arr[j + 1]);
                // Troca os elementos se estiverem fora de ordem
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Método de ordenação: Bubble Sort recursivo
void bubbleSortRecursive(int arr[], int n) {
    // Caso base: se o tamanho da array for 1, ela já está ordenada
    if (n == 1)
        return;

    // Percorre a array e move o maior elemento para o final
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            // Troca os elementos se estiverem fora de ordem
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    // Chama a função recursivamente com um tamanho menor
    bubbleSortRecursive(arr, n - 1);
}

/*  Selection Sort ou Ordenação por seleção
 - A cada, passo procura o menor elemento da parte não ordenada
   e coloca na seguinte posição da parte ordenada e repete até ordenar tudo.
 - Não é estável
 - Versão recursiva é mais lenta que a versão iterativa
 - Ineficiente para arrays grandes

    Complexibilidade
 - Melhor caso: O(N^2)
 - Caso médio: O(N^2)
 - Pior caso: O(N^2)
*/

// Método de ordenação: Selection Sort
// Pseudocódigo:
// Função SelectionSort(lista):
//     Para cada elemento i do início até o penúltimo da lista:
//         índice_minimo = i
//         Para cada elemento j de i+1 até o final da lista:
//             Se lista[j] < lista[índice_minimo]:
//                 índice_minimo = j

//         Se índice_minimo diferente de i:
//             Trocar lista[i] com lista[índice_minimo]

//     Retornar lista

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        // Supõe que o índice atual é o mínimo
        int minIndex = i;
        // Encontra o índice do elemento mínimo na parte não ordenada
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // swap(&arr[i], &arr[minIndex]);
        // Troca o elemento mínimo encontrado com o primeiro elemento
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

// Método de ordenação: Selection Sort recursivo
void selectionSortRecursive(int arr[], int n, int i) {
    // Caso base: se o índice atingiu o final da array
    if (i == n - 1)
        return;

    // Supõe que o índice atual é o mínimo
    int minIndex = i;

    // Encontra o índice do elemento mínimo na parte não ordenada
    for (int j = i + 1; j < n; j++) {
        if (arr[j] < arr[minIndex]) {
            minIndex = j;
        }
    }
    // swap(&arr[i], &arr[minIndex]);
    if (minIndex != i) {
            // Troca o elemento mínimo encontrado com o primeiro elemento
            arr[i] = arr[i] + arr[minIndex];
            arr[minIndex] = arr[i] - arr[minIndex];
            arr[i] = arr[i] - arr[minIndex];
        }
    // Chama a função recursivamente com o próximo índice
    selectionSortRecursive(arr, n, i + 1);
}

/*  Insertion Sort ou Ordenação por inserção
 - Percorre o array e insere cada elemento na posição correta
   da parte ordenada (semelhante a carta de baralho).
 - Estável
 - Versão recursiva é mais lenta que a versão iterativa
 - Ineficiente para arrays grandes

    Complexibilidade
 - Melhor caso: O(N)
 - Caso médio: O(N^2)
 - Pior caso: O(N^2)
*/  

// Método de ordenação: Insertion Sort
// Pseudocódigo:
// Função InsertionSort(lista):
//     Para cada elemento i de 1 até o final da lista:
//         valor_atual = lista[i]
//         j = i - 1

//         Enquanto j >= 0 e lista[j] > valor_atual:
//             lista[j + 1] = lista[j]
//             j = j - 1

//         lista[j + 1] = valor_atual

//     Retornar lista

void insertionSort(int arr[], int n) {
    int key, j;
    for (int i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Método de ordenação: Insertion Sort recursivo
void insertionSortRecursive(int arr[], int n) {
    // Caso base: se o tamanho da array for 1, ela já está ordenada
    if (n <= 1)
        return;

    // Ordena os primeiros n-1 elementos
    insertionSortRecursive(arr, n - 1);

    // Insere o último elemento na posição correta
    int lastElement = arr[n - 1];
    int j = n - 2;

    // Move os elementos maiores que lastElement para a direita
    while (j >= 0 && arr[j] > lastElement) {
        arr[j + 1] = arr[j];
        j--;
    }

    // Insere lastElement na posição correta
    arr[j + 1] = lastElement;
}

/*  Quick Sort ou Ordenação rápida
 - Escolhe um elemento como pivô e particiona a array ao redor dele.
   Menores antes dele e maiores depois dele (divisão e conquista).
 - Não é estável
 - Recursivamente ordena as duas partes
 - Ineficiente para arrays grandes
 - Desvantagem: como escolher o pivô?

    Complexibilidade
 - Melhor caso: O(N log N)
 - Caso médio: O(N log N)
 - Pior caso(raro): O(N^2)
*/

// Método de ordenação: Quick Sort
// Pseudocódigo:
// Função quickSort(array, início, fim)
//    Se início < fim
//       Pivô = particionar(array, início, fim)
//       quickSort(array, início, Pivô - 1)
//       quickSort(array, Pivô + 1, fim)

// Função particionar(array, início, fim)
//    Pivô = array[fim]
//    ÍndicePivô = início

//    Para i de início até fim - 1
//       Se array[i] <= Pivô
//          Trocar array[i] com array[ÍndicePivô]
//          Incrementar ÍndicePivô

//    Trocar array[ÍndicePivô] com array[fim]

//    Retornar ÍndicePivô

// Função para encontrar a posição correta do pivô no array
// Nesse caso, o pivô é o primeiro elemento
int partition(int arr[], int low, int high) {
    int pivot = arr[low];
    int i = low + 1;

    for (int j = low + 1; j <= high; j++) {
        if (arr[j] < pivot) {
            // swap(&arr[i], &arr[j]);
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
            i++;
        }
    }

    // swap(&arr[low], &arr[i - 1]);
    // Troca o pivô com o elemento na posição correta
    arr[low] = arr[i - 1];
    arr[i - 1] = pivot;
    return i - 1;
}

// Função principal do Quick Sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Encontra a posição do pivô
        int pi = partition(arr, low, high);

        // Recursivamente ordena os elementos antes e depois do pivô
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

/*  Merge Sort ou Ordenação por fusão
 - Divide o array em duas partes iguais, até que cada subcojunto
   contenha apenas um elemento, e depois intercala os subconjuntos
   para produzir o array ordenada.
 - Estável
 - Recursivamente ordena as duas partes
 - Desvantegem: recursivo e usa um vetor auxiliar durante a ordenação

    Complexibilidade
 - Melhor caso: O(N log N)
 - Caso médio: O(N log N)
 - Pior caso: O(N log N)
*/

// Método de ordenação: Merge Sort
// Pseudocódigo:
// Procedimento mergeSort(arr: Lista):
//     Se o comprimento da lista for 1 ou menor:
//         Retorne a lista (já está ordenada)

//     Divida a lista em duas metades, chamaremos de esquerda e direita
//     Esquerda = Sublista contendo os primeiros n/2 elementos de arr
//     Direita = Sublista contendo os elementos restantes

//     // Recursivamente, aplique mergeSort nas duas metades
//     Esquerda = mergeSort(Esquerda)
//     Direita = mergeSort(Direita)

//     // Combine as duas metades ordenadas
//     Retorne merge(Esquerda, Direita)

// Procedimento merge(Esquerda: Lista, Direita: Lista):
//     Crie uma nova lista vazia chamada resultado

//     Enquanto Esquerda não está vazia e Direita não está vazia:
//         Se o primeiro elemento de Esquerda for menor que o primeiro elemento de Direita:
//             Adicione o primeiro elemento de Esquerda ao resultado
//             Remova o primeiro elemento de Esquerda
//         Senão:
//             Adicione o primeiro elemento de Direita ao resultado
//             Remova o primeiro elemento de Direita

//     // Adicione os elementos restantes, se houver, de Esquerda e Direita
//     Adicione todos os elementos restantes de Esquerda ao resultado
//     Adicione todos os elementos restantes de Direita ao resultado

//     Retorne resultado

// Função para mesclar duas sublistas ordenadas
void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Criação de sublistas temporárias
    int L[n1], R[n2];

    // Copia dados para as sublistas temporárias L[] e R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Mescla as sublistas de volta em arr[l..r]
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copia os elementos restantes de L[], se houver algum
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copia os elementos restantes de R[], se houver algum
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Função principal para realizar o Merge Sort recursivo
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        // Encontra o ponto médio do array
        int m = l + (r - l) / 2;

        // Ordena a primeira e a segunda metades
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        // Mescla as metades ordenadas
        merge(arr, l, m, r);
    }
}

/*  Heap Sort ou Ordenação por seleção
 - O Heap Sort é um algoritmo de ordenação que utiliza uma estrutura de 
   dados chamada heap. Heap é uma árvore binária especial onde o valor de 
   cada nó é no máximo (para um Max Heap) ou no mínimo (para um Min Heap) 
   o valor de seus filhos.
 - Não é estável
 - Versão iterativa é mais rápida que a versão recursiva
 - Desvantagem: não é estável e usa um vetor auxiliar durante a ordenação

    Complexibilidade
 - Melhor caso: O(N log N)
 - Caso médio: O(N log N)
 - Pior caso: O(N log N)
*/

// Método de ordenação: Heap Sort
// Pseudocódigo:
// procedimento heapify(arr: vetor, n: inteiro, i: inteiro)
//     maior = i
//     filho_esquerdo = 2 * i + 1
//     filho_direito = 2 * i + 2

//     se filho_esquerdo < n e arr[filho_esquerdo] > arr[maior]
//         maior = filho_esquerdo

//     se filho_direito < n e arr[filho_direito] > arr[maior]
//         maior = filho_direito

//     se maior ≠ i
//         trocar(arr[i], arr[maior])
//         heapify(arr, n, maior)

// procedimento heapSort(arr: vetor, n: inteiro)
//     para i de n / 2 - 1 até 0 passo -1
//         heapify(arr, n, i)

//     para i de n - 1 até 1 passo -1
//         trocar(arr[0], arr[i])
//         heapify(arr, i, 0)

// vetor_a_ordenar = [4, 10, 3, 5, 1]
// tamanho_do_vetor = comprimento(vetor_a_ordenar)

// heapSort(vetor_a_ordenar, tamanho_do_vetor)

// Função para fazer o heapify de uma subárvore com raiz em i
void heapify(int arr[], int n, int i) {
    int largest = i; // Inicializa o maior como a raiz
    int left = 2 * i + 1; // índice do filho esquerdo
    int right = 2 * i + 2; // índice do filho direito

    // Se o filho esquerdo é maior que a raiz
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // Se o filho direito é maior que a raiz
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Se o maior não é a raiz
    if (largest != i) {
        // Troca a raiz com o maior
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        // Recursivamente heapify na subárvore afetada
        heapify(arr, n, largest);
    }
}

// Função principal para ordenar um array usando o Heap Sort
void heapSort(int arr[], int n) {
    // Constrói o heap (reorganiza o array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extrai elementos do heap um por um
    for (int i = n - 1; i > 0; i--) {
        // Move a raiz atual para o final
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        // Chama o heapify na heap reduzida
        heapify(arr, i, 0);
    }
}


// -------------------------------------------- 

// Função auxiliar para imprimir um array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {

    setlocale(LC_NUMERIC, "C");

    // Seed para números aleatórios
    srand(time(NULL));

    // Cria um array de números aleatórios
    int sizes[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 
    6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000, 300000, 400000, 500000, 
    600000, 700000, 800000, 900000, 1000000};
    int* arr = NULL;
    int size = 0;
    clock_t start, end;
    double cpu_time_used;

    for (size_t i = 0; i < sizeof(sizes) / sizeof(sizes[0]); i++) {
        size = sizes[i];
        arr = malloc(size * sizeof(int));
        for (int j = 0; j < size; j++) {
            arr[j] = rand() % 100;  // Números aleatórios entre 0 e 99
        }

        // Bubble Sort
        start = clock();
        bubbleSort(arr, size);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Bubble Sort, %d, %f\n", size, cpu_time_used);

        // Bubble Sort Recursivo
        start = clock();
        bubbleSortRecursive(arr, size);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Bubble Sort Recursivo, %d, %f\n", size, cpu_time_used);
        
        // Selection Sort
        start = clock();
        selectionSort(arr, size);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Selection Sort, %d, %f\n", size, cpu_time_used);

        // Selection Sort Recursivo
        start = clock();
        selectionSortRecursive(arr, size, 0);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Selection Sort Recursivo, %d, %f\n", size, cpu_time_used);

        // Insertion Sort
        start = clock();
        insertionSort(arr, size);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Insertion Sort, %d, %f\n", size, cpu_time_used);

        // Insertion Sort Recursivo
        start = clock();
        insertionSortRecursive(arr, size);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Insertion Sort Recursivo, %d, %f\n", size, cpu_time_used);

        // Quick Sort
        start = clock();
        quickSort(arr, 0, size - 1);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Quick Sort, %d, %f\n", size, cpu_time_used);

        // Merge Sort
        start = clock();
        mergeSort(arr, 0, size - 1);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Merge Sort, %d, %f\n", size, cpu_time_used);

        // Heap Sort
        start = clock();
        heapSort(arr, size);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Heap Sort, %d, %f\n", size, cpu_time_used);

        // Libera a memória alocada para o array
        free(arr);
    }
    return 0;
}