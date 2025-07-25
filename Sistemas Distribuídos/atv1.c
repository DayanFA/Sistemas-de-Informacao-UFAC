#include <stdio.h>
#include <string.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int rank, tag=0;
    int a, b;
    int resultado;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        a = 2;
        b = 3;
        MPI_Send(&a, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
        MPI_Send(&a, 1, MPI_INT, 2, tag, MPI_COMM_WORLD);
        MPI_Send(&b, 1, MPI_INT, 2, tag, MPI_COMM_WORLD);
        MPI_Send(&b, 1, MPI_INT, 3, tag, MPI_COMM_WORLD);
    } else if (rank == 1) {
        MPI_Recv(&a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        resultado = (a * a)-2;
        printf("Processo 1 ((a^2)-2): %d\n", resultado);
    } else if (rank == 2) {
        MPI_Recv(&a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        MPI_Recv(&b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        resultado = (2 * a * b)+2;
        printf("Processo 2 ((2ab)+2): %d\n", resultado);
    } else if (rank == 3) {
        MPI_Recv(&b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        resultado = (b * b)/2;
        printf("Processo 3 ((b^2)/2): %d\n", resultado);
    }

    MPI_Finalize();
    return 0;
}