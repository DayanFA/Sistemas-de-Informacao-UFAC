import matplotlib.pyplot as plt

# Função para ler os dados do arquivo e plotar
def plot_fitness(filename, title):
    temperatures = []
    fitness_values = []

    with open(filename, 'r') as file:
        for line in file:
            temperature, fitness = line.split()
            temperatures.append(float(temperature))
            fitness_values.append(float(fitness))

    plt.plot(temperatures, fitness_values, label=title)

# Plotar os dados de Hill Climbing
plot_fitness('C:\\Users\\dolby\\OneDrive\\Área de Trabalho\\output\\hill_climbing_fitness.txt', 'Hill Climbing')

# Plotar os dados de Simulated Annealing
plot_fitness('C:\\Users\\dolby\\OneDrive\\Área de Trabalho\\output\\simulated_annealing_fitness.txt', 'Simulated Annealing')

plt.xlabel('Temperature')
plt.ylabel('Fitness')
plt.title('Fitness over Temperature')
plt.legend()
plt.show()