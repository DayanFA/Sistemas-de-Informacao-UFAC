#include <stdio.h> // print, fgets function
#include <string.h> //strlen, memcpy function
#include <math.h> // sqrt, pow, cos, exp, M_PI
#include <time.h> // time function
#include <stdlib.h> // rand, srand function

void tweak(double* sol);
void initialize(double* sol);

double ackley(double* sol);
double rosenbrock(double* sol);
double rastrigin(double* sol);
double griewank(double* sol);

double fitness(double* sol){
  return griewank(sol);
}

//min - max values per function
//ackley [-32.768, 32.768]
//griewank [-600, 600]
//rastrigin [-5.12, 5.12]
//rosenbrock [-5, 10]

int dimension=10;
double min=-600;
double max=600;

void hill_climbing(double* sol); 
void simulated_annealing(double* sol); 

int main(){
    srand(time(NULL));
    double sol[dimension];
    initialize(sol);

    // Hill Climbing
    hill_climbing(sol);

    // Simulated Annealing
    simulated_annealing(sol);

    printf("Print solution:\t");
    for(int i=0;i<dimension;i++)
        printf("%f ", sol[i]);
    printf("Fitness: %f\n",fitness(sol));

    return 0;
}

void initialize(double *sol){
    for (int i = 0; i < dimension; i++) {
        sol[i] = min + (max - min) * ((double)rand() / RAND_MAX); 
    }
}

void tweak(double *sol){
    double p = 1.0; 
    double r = 0.1; 
    for (int i = 0; i < dimension; i++) { 
        if (p >= ((double)rand() / RAND_MAX)) { 
            double n;
            do {
                n = r * (2.0 * ((double)rand() / RAND_MAX) - 1.0); 
            } while (sol[i] + n < min || sol[i] + n > max); 
            sol[i] += n; 
        }
    }
}

void hill_climbing(double* sol) {
    FILE *file = fopen("hill_climbing_fitness.txt", "w"); 
    double current_fitness = fitness(sol); 
    double new_sol[dimension];
    for (int i = 0; i < 1000; i++) { 
        memcpy(new_sol, sol, dimension * sizeof(double)); 
        tweak(new_sol); 
        double new_fitness = fitness(new_sol); 
        if (new_fitness < current_fitness) { 
            memcpy(sol, new_sol, dimension * sizeof(double));
            current_fitness = new_fitness;
        }
        fprintf(file, "%d %f\n", i, current_fitness); 
    }
    fclose(file); 
}

void simulated_annealing(double* sol) {
    FILE *file = fopen("simulated_annealing_fitness.txt", "w"); 
    double temperature = 1000.0; 
    double cooling_rate = 0.99; 
    double current_fitness = fitness(sol); 
    double best_fitness = current_fitness; 
    double new_sol[dimension];
    double best_sol[dimension];
    memcpy(best_sol, sol, dimension * sizeof(double));

    while (temperature > 0.1) { 
        memcpy(new_sol, sol, dimension * sizeof(double)); 
        tweak(new_sol); 
        double new_fitness = fitness(new_sol); 

        if (new_fitness > current_fitness || exp((current_fitness - new_fitness) / temperature) > ((double)rand() / RAND_MAX)) { 
            memcpy(sol, new_sol, dimension * sizeof(double)); 
            current_fitness = new_fitness;
        }

        if (current_fitness > best_fitness) { 
            best_fitness = current_fitness;
            memcpy(best_sol, sol, dimension * sizeof(double)); 
        }

        temperature *= cooling_rate; 
        fprintf(file, "%f %f\n", temperature, best_fitness); 
        printf("Temperature: %f, Current Fitness: %f, Best Fitness: %f\n", temperature, current_fitness, best_fitness); // Mensagem de depuração
    }

    memcpy(sol, best_sol, dimension * sizeof(double)); 
    fclose(file); 
}
//adapted from jmetal
double griewank(double *sol){
    double sum = 0.0;
    double mult = 1.0;
    double d = 4000.0;
    for (int var = 0; var < dimension; var++){
      sum += sol[var]*sol[var];    
      mult *= cos(sol[var]/sqrt(var+1));    
    }

    return 1.0/d * sum - mult + 1.0;
}

//adapted from jmetal
double rastrigin(double* sol){
    double result = 0.0;
    double a = 10.0;
    double w = 2*M_PI;

    for (int i = 0; i < dimension; i++) {
      result += sol[i]*sol[i] - a*cos(w*sol[i]);
    }
    result += a*dimension;

    return result;
}

//adapted from jmetal
double rosenbrock(double* sol){
    double sum = 0.0;
    for (int i = 0; i < dimension - 1; i++) {
      sum += 100.0 * (sol[i+1]-sol[i]*sol[i])*(sol[i+1]-sol[i]*sol[i]) +(sol[i]-1)*(sol[i]-1) ;
    }
    return sum;
}

//adapted from math function
double ackley(double* sol){
    double a=20;
    double b=0.2;
    double c=2*M_PI;
    double sum1 = 0;
    double sum2 = 0;
    for (int i = 0; i < dimension; i++) {
        sum1 += pow(sol[i], 2);
        sum2 += cos(c*sol[i]);
    }
    return -a*exp(-b*sqrt(sum1/dimension)) - exp(sum2/dimension) + a + exp(1.0);
}