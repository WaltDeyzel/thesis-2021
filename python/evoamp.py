import numpy as np 
from functions import *
class EvoAmp:
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
        self.pop_pha = np.random.uniform(size = (self.population_tot, self.N), low = 0, high = 2*np.pi*0) # randians
        
        # Amplitude of the signal of each antenna element. 
        self.pop_amp = np.random.uniform(size=(self.population_tot, self.N), low = 0, high=1)
        
        # Population with same spacing and phase -> Only optimizing amplitude
        for i in range(self.population_tot):
            self.pop_dis[i, :] = d
            
        # Fitness scores
        self.pop_fit = np.zeros(self.population_tot, dtype = np.float)
        
        self.evolve()
    
    def results(self):
        # Return the best solution
        q = np.argmin(self.pop_fit)
        return self.pop_amp[q]
        
    def evolve(self):
        # probabilities for cross over. To avoid calculationg random numbers every itteration.
        crossovers = np.random.uniform(size=(self.generations), low = 0, high=1)
        mutations = np.random.uniform(size=(self.generations), low = 0, high=1)
        
        for i in range(self.generations):
            # Calculate the fitness score of each solution
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.target)
                self.pop_fit[dna] = score;
            # Index of fittest solution   
            index = np.argmin(self.pop_fit)
            # Copy fitteset solution over to next genertation (first and last index of array)
            self.pop_amp[0] = self.pop_amp[index]
            self.pop_amp[-1] = self.pop_amp[index]
           
            # Stop simulating when the generation matches the maximun no of generations.   
            if i == self.generations-1:
                print('DONE')
                break
            
            # Itterations per generations
            for _ in range(1):
                
                if crossovers[i] < self.crossover_rate:
                    # crossover occurs (Two parent solutions)
                    s_1 = selection(self.pop_fit)
                    s_2 = selection(self.pop_fit)
                    self.pop_amp[s_1] = (self.pop_amp[s_1] + self.pop_amp[s_2])/2

                if mutations[i] < self.mutation_rate:
                    # mutation occurs
                    s_1 = selection(self.pop_fit)
                    self.pop_amp[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=1)
                    
        

def fitnessX(ddd, alpha, I, target):
    return SLL2(ddd, alpha, I) + HPBW(ddd, alpha, I)
     
    

if __name__ == '__main__':
    #d = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
    # ----
    d = np.array([0.3,	0.475, 0.52, 0.475, 0.3]) 
    #d = np.array([0.425,	0.475,	0.5,	0.475, 0.425])
    #d = np.array([0.35,	0.48,	0.56,	0.48, 0.35])
    
    #p = np.array([0, 0, 0, 0, 0, 0])
    # CA 
    p = np.array([230, 105, 315, 193, 40, 277])*np.pi/180
    #p = np.array([250, 104, 316, 162, 15, 231])*np.pi/180
    #p = np.array([138, 20, 211, 59, 275, 133])*np.pi/180
    
    #p = np.array([])
    target = 90
    N = 6;
    # Constants
    
    sims = 10
    best_a = np.zeros((sims, N), dtype=float)

    # Spacing and Phase
    for i in range(sims):
        evo = EvoAmp(2, 0, 1, 10000, N, d, target)
        amp = evo.results()
        best_a[i] = amp
        
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    hpbw = np.zeros((sims), dtype=float)
    sll = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = SLL2(d, p, best_a[i])#fitnessX(d, p, best_a[i], target)
        hpbw[i] = HPBW(d, p, best_a[i])
        sll[i] = SLL(d, p, best_a[i])
        
   
    # select fittest solution    
    q = np.argmin(fit)
    
    print('RESULTS')
    print(best_a[q])
    print(best_a)
    showUniform(33)
    show(d,  p, best_a[q])
    
    
    from wexcel import *
    date_file = 'AMP.xlsx'
    
    # save_data(best_a, date_file, 'amp')
    # #save_data([HPBW(d, p, best_a[q]), SLL(d, p, best_a[q])], date_file, 'hpbw')
    # #save_data(fit, date_file, 'fit')
    # save_data(hpbw, date_file, 'hpbw')
    # save_data(sll, date_file, 'sll')
    
    
    print('SLL', SLL(d, p, best_a[q]))
    print('HPBW',HPBW(d, p, best_a[q]))
    plt.show()