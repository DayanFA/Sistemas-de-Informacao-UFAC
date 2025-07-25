#include <stdio.h>
#include <string.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int rank, tag=0;
    int A[2][2] = {{1, 2}, {3, 4}};
    int B[2][2] = {{5, 6}, {7, 8}};
    int C[2][2];
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        MPI_Send(&A, 4, MPI_INT, 1, tag, MPI_COMM_WORLD);
        MPI_Send(&B, 4, MPI_INT, 1, tag, MPI_COMM_WORLD);
    } else if (rank == 1) {
        MPI_Recv(&A, 4, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        MPI_Recv(&B, 4, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                C[i][j] = A[i][j] + B[i][j];

        printf("Resultado da soma das matrizes:\n");
        for (int i = 0; i < 2; i++)
            printf("%d %d\n", C[i][0], C[i][1]);
    }

    MPI_Finalize();
    return 0;
}