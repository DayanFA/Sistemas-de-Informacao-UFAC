#include <stdio.h>
#include <string.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int rank, a, b, tag=0;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 1) {
        a = 10;  
        MPI_Send(&a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD);
    } else if (rank == 2) {
        b = 2;  
        MPI_Send(&b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD);
    } else if (rank == 0) {
        MPI_Recv(&a, 1, MPI_INT, 1, tag, MPI_COMM_WORLD, &status);
        MPI_Recv(&b, 1, MPI_INT, 2, tag, MPI_COMM_WORLD, &status);

        printf("Soma: %d\n", a + b);
        printf("Subtração: %d\n", a - b);
        printf("Multiplicação: %d\n", a * b);
        if (b != 0)
            printf("Divisão: %.2f\n", (float)a / b);
        else
            printf("Divisão: Indefinida (divisão por zero)\n");
    }

    MPI_Finalize();
    return 0;
}
