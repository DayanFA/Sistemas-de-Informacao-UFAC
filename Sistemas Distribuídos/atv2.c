#include <stdio.h>
#include <string.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int rank, tag=0;
    float distancia, tempo, velocidade;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 1) {
        distancia = 100.0;
        MPI_Send(&distancia, 1, MPI_FLOAT, 0, tag, MPI_COMM_WORLD);
    } else if (rank == 2) {
        tempo = 2.0;
        MPI_Send(&tempo, 1, MPI_FLOAT, 0, tag, MPI_COMM_WORLD);
    } else if (rank == 0) {
        MPI_Recv(&distancia, 1, MPI_FLOAT, 1, tag, MPI_COMM_WORLD, &status);
        MPI_Recv(&tempo, 1, MPI_FLOAT, 2, tag, MPI_COMM_WORLD, &status);
        if (tempo != 0) {
            velocidade = distancia / tempo;
            printf("Velocidade = %.2f m/s\n", velocidade);
        } else {
            printf("Erro: tempo igual a zero.\n");
        }
    }

    MPI_Finalize();
    return 0;
}