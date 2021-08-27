import simulate.*

population_total = 500;
crossover_rate = 0.5;
mutation_rate = 0.1;
simulations = 50;

simulate(population_total, crossover_rate, mutation_rate, simulations, 30, '27Aug/sim60deg1.xlsx')
simulate(population_total, crossover_rate, mutation_rate, simulations, 30, '27Aug/sim60deg2.xlsx')
simulate(population_total, crossover_rate, mutation_rate, simulations, 30, '27Aug/sim60deg3.xlsx')

simulate(population_total, crossover_rate, mutation_rate, simulations, 20, '27Aug/sim80deg1.xlsx')
simulate(population_total, crossover_rate, mutation_rate, simulations, 20, '27Aug/sim80deg2.xlsx')
simulate(population_total, crossover_rate, mutation_rate, simulations, 20, '27Aug/sim80deg3.xlsx')
