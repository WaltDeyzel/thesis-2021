import numpy as np 
from evolution import selection, fitness
from functions import *
import time
class EvoPhase:
    #Initiate parameters
    def __init__(self, population_tot, crossover_rate, mutation_rate, generations, N, d, target):
        self.population_tot = population_tot
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.N = N
        self.target = target
   
        # Spacing between antennas 
        self.pop_dis = np.ndarray(shape=(self.population_tot, self.N-1))
       
        # Phase Shift of the signal of each antenna element
        self.pop_pha = np.random.uniform(size = (self.population_tot, self.N), low = 0, high = 2*np.pi) # randians
        
        # Amplitude of the signal of each antenna element. 
        self.pop_amp = np.ndarray(shape=(self.population_tot, self.N))
        # Uinform amplitude
        amp = np.array([1, 1, 1, 1, 1, 1])
        
        # Population with same spacing and amplitude -> Only optimizing phase
        for i in range(self.population_tot):
            self.pop_dis[i, :] = d
            self.pop_amp[i, :] = amp
            
        # Fitness scores 
        self.pop_fit = np.zeros(self.population_tot, dtype = np.float)
        self.params = np.zeros(self.generations, dtype = np.float)
        self.evolve()
    
    def results(self):
        # Return the best solution
        q = np.argmin(self.pop_fit)
        return self.pop_pha[q]
    
    def getParams(self):
        return self.params

    def evolve(self):
        # probabilities for crossover. To avoid calculationg random numbers every itteration.
        crossovers = np.random.uniform(size=(self.generations), low = 0, high=1)
        mutations = np.random.uniform(size=(self.generations), low = 0, high=1)
        
        for i in range(self.generations):
            tot = 0
            # Calculate the fitness score of each solution 
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.target)
                self.pop_fit[dna] = score;
                tot += score
            # Index of fittest solution
            index = np.argmin(self.pop_fit)
            # Copy fitteset solution over to next genertation (first and last index of array)
            self.pop_pha[0] = self.pop_pha[index]
            self.pop_pha[-1] = self.pop_pha[index]
            self.params[i] = self.pop_fit[index]
            # Stop simulating when the generation matches the maximun no of generations.   
            if i == self.generations-1:
                print('DONE')
                break
            
            # Itterations per generations
            for _ in range(10):
                if crossovers[i] < self.crossover_rate:
                    # crossover occurs (Two parent solutions)
                    s_1 = selection(self.pop_fit)
                    s_2 = selection(self.pop_fit)
                    # Ofspring 
                    A = 0.99
                    if self.pop_fit[s_1] < self.pop_fit[s_2]:
                        self.pop_pha[s_1]= self.pop_pha[s_1] * A + self.pop_pha[s_2] * (1-A)
                    else:
                        self.pop_pha[s_1] = self.pop_pha[s_1] * (1-A) + self.pop_pha[s_2] * A

                if mutations[i] < self.mutation_rate:
                    # mutation occurs
                    s_1 = selection(self.pop_fit)
                    self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
        


     
    

if __name__ == '__main__': 
    # ----
    #d = np.array([0.3,	0.475, 0.52, 0.475, 0.3]) 
    #d = np.array([0.425,	0.475,	0.5,	0.475, 0.425])
    #d = np.array([0.35,	0.48,	0.56,	0.48, 0.35])
    I = np.array([1, 1, 1, 1, 1, 1])


    #d = np.array([0.3,	0.525,	0.5,	0.525, 0.525])
    d = np.array([0.5, 0.5, 0.5, 0.5, 0.5])


    target = 45
    N = 6;
    # Constants
    gens = 1000
    sims = 3
    best_p = np.zeros((sims, N), dtype=float)
    par = np.zeros((sims, gens), dtype=float)
    # Spacing and Phase
    start = time.time()

    for i in range(sims):
        evo = EvoPhase(2, 0, 1, gens, N, d, target)
        par[i] = evo.getParams()
        pha = evo.results()
        best_p[i] = pha
    
    finish = time.time()   
    print('Time : ' , finish - start)
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    hpbw = np.zeros((sims), dtype=float)
    sll = np.zeros((sims), dtype=float)
    sll2 = np.zeros((sims), dtype=float)
    directivity = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = SLL2(d, best_p[i], I) #fitness(d, best_p[i], I, target)#SLL(d, best_p[i], I)#
        hpbw[i] = HPBW(d, best_p[i], I)
        sll[i] = SLL(d, best_p[i], I)
        sll2[i] = SLL2(d, best_p[i], I)
        directivity[i] = getDirectivity(d, best_p[i], I, target)
        
     
    # Display fittest solution
    # select fittest solution    
    q = np.argmin(fit)
    print('hpbw', hpbw[q])
    print('sll', sll[q])
    
    from wexcel import *
    date_file = 'param.xlsx'
    
    # save_data(best_p, date_file, 'pha')
    # save_data(hpbw, date_file, 'hpbw')
    # save_data(sll, date_file, 'sll')
    # save_data(sll2, date_file, 'sll2')
    # save_data(directivity, date_file, 'dir')
    save_data(par.T, date_file, 'par')
    
    
    showUniform(target)
    show(d,  best_p[q],  I)
    plt.show()
    print(best_p)
    
    plt.plot(par.T)
    plt.show()