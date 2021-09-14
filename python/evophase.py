import numpy as np 
from scipy.stats import norm
from evolution import selection, fitness
from functions import *
class EvoPhase:
    
    def __init__(self, population_tot, crossover_rate, mutation_rate, generations, N, d, target):
        self.population_tot = population_tot
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.N = N
        self.target = target
        
        # Spacing between 
        self.pop_dis = np.ndarray(shape=(self.population_tot, self.N-1))
       
        # Phase Shift
        self.pop_pha = np.random.uniform(size = (self.population_tot, self.N), low = 0, high = 2*np.pi) # randians
        
        self.pop_amp = np.ndarray(shape=(self.population_tot, self.N))
        amp = np.array([1, 1, 1, 1, 1, 1])
        
        for i in range(self.population_tot):
            self.pop_dis[i, :] = d
            self.pop_amp[i, :] = amp
            
        # Fitness
        self.pop_fit = np.zeros(self.population_tot, dtype = np.float)
        
        self.evolve()
    
    def results(self):
        q = np.argmin(self.pop_fit)
        return self.pop_pha[q]
        
    def evolve(self):
        # probabilities for cross over. To avoid calculationg random numbers every itteration.
        crossovers = np.random.uniform(size=(self.generations), low = 0, high=1)
        mutations = np.random.uniform(size=(self.generations), low = 0, high=1)
        
        index = 0;
        fittest = 0
        for i in range(self.generations):
            
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.target)
                self.pop_fit[dna] = score;
                if score < fittest:
                    fittest = score
                    index = dna
            
            self.pop_pha[0] = self.pop_pha[index]
           
             
            if i == self.generations-1:
                print('DONE')
                break
            
            if crossovers[i] < self.crossover_rate:
                # crossover occurs
                    s_1 = selection(self.pop_fit)
                    s_2 = selection(self.pop_fit)
                    #self.pop_pha[s_1] = np.divide(self.pop_pha[s_1] + self.pop_pha[s_2],2)
                    self.pop_pha[s_1][3:5] = (self.pop_pha[s_1][3:5] + self.pop_pha[s_2][3:5])/2
                    self.pop_pha[s_2][0:2] = (self.pop_pha[s_1][0:2] + self.pop_pha[s_2][0:2])/2

            if mutations[i] < self.mutation_rate:
                # mutation occurs
                s_1 = selection(self.pop_fit)
                self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
        


     
    

if __name__ == '__main__':
    d = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
    I = np.array([1, 1, 1, 1, 1, 1])

    target = 60
    N = 6;
    # Constants
    
    sims = 5
    best_p = np.zeros((sims, N), dtype=float)

    # Spacing and Phase
    for i in range(sims):
        evo = EvoPhase(100, 0.5, 0.05, 100, N, d, target)
        pha = evo.results()
        best_p[i] = pha
        
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = fitness(d, best_p[i], I, target)
     
    results(d, best_p, I, fit)
    # Display fittest solution
    # select fittest solution    
    q = np.argmin(fit)
    
    show(d,  best_p[q],  I)
    plt.show()
    print(best_p)