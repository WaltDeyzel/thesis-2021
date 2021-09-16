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
        self.pop_pha = np.random.uniform(size = (self.population_tot, self.N), low = 0, high = 2*np.pi*0) # randians
        
        # Amplitude 
        self.pop_amp = np.random.uniform(size=(self.population_tot, self.N), low = 0, high=1)
        
        for i in range(self.population_tot):
            self.pop_dis[i, :] = d
            
        # Fitness
        self.pop_fit = np.zeros(self.population_tot, dtype = np.float)
        
        self.evolve()
    
    def results(self):
        q = np.argmin(self.pop_fit)
        return self.pop_amp[q]
        
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
            
            self.pop_amp[0] = self.pop_amp[index]
           
             
            if i == self.generations-1:
                print('DONE')
                break
            
            if crossovers[i] < self.crossover_rate:
                # crossover occurs
                    s_1 = selection(self.pop_fit)
                    s_2 = selection(self.pop_fit)
                    self.pop_amp[s_1] = (self.pop_amp[s_1] + self.pop_amp[s_2])/2

            if mutations[i] < self.mutation_rate:
                # mutation occurs
                s_1 = selection(self.pop_fit)
                self.pop_amp[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=1)
        


     
    

if __name__ == '__main__':
    d = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
    p = np.array([0, 0, 0, 0, 0, 0])

    target = 90
    N = 6;
    # Constants
    
    sims = 10
    best_a = np.zeros((sims, N), dtype=float)

    # Spacing and Phase
    for i in range(sims):
        evo = EvoPhase(1000, 0.5, 0.1, 1000, N, d, target)
        amp = evo.results()
        best_a[i] = amp
        
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = fitness(d, p, best_a[i], target)
   
    # select fittest solution    
    q = np.argmin(fit)
    
    print('RESULTS')
    print(best_a[q])
    print(best_a)
    show(d,  p, best_a[q])
    show(d,  p, np.array([1, 1, 1, 1, 1, 1]))
    
    from wexcel import *
    date_file = 'amp_3.xlsx'
    
    save_data(best_a, date_file, 'amp')
    save_data([HPBW(d, p, best_a[q]), SLL(d, p, best_a[q])], date_file, 'hpbw')
    
    print('SLL', SLL(d, p, best_a[q]))
    print('HPBW',HPBW(d, p, best_a[q]))
    plt.show()