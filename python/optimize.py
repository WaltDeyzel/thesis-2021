import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import normalize

from functions import *

global LOW, HIGH
LOW = 0.25
HIGH = 1.5

class Evolution:
    
    def __init__(self, population_tot, crossover_rate, mutation_rate, generations, N, target):
        self.population_tot = population_tot
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.N = N
        self.target = target
        
        # Spacing between 
        #self.pop_dis = np.random.uniform(size=(self.population_tot, self.N-1), low = LOW, high=HIGH)
        self.pop_dis = np.ndarray(shape=(self.population_tot, self.N-1))
        
        # Phase Shift
        self.pop_pha = np.random.uniform(size = (self.population_tot, self.N), low = 0, high = 2*np.pi) # randians
        #self.pop_pha = np.ndarray(shape=(self.population_tot, self.N))
        
        # Amplitude 
        self.pop_amp = np.random.uniform(size=(self.population_tot, self.N), low = 1, high=1)
        #self.pop_amp = np.ndarray(shape=(self.population_tot, self.N))
        
        for i in range(self.population_tot):
            self.pop_dis[i, :] = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
            #self.pop_pha[i, :] = np.array([1, 1, 1, 1, 1, 1])
            #self.pop_amp[i, :] = np.array([1, 1, 1, 1, 1, 1])
            
        # print(self.pop_dis)
        # print(self.pop_pha)
        # print(self.pop_amp) 
        
        # Fitness
        self.pop_fit = np.zeros(self.population_tot, dtype = np.float)
        
        standard_deviation = 5
        x_values = np.arange(0, 180, 1)
        y_values = norm(target, standard_deviation) 
        self.ideal = np.array(y_values.pdf(x_values))/np.max(np.array(y_values.pdf(x_values)))
        
        self.evolve()
    
    def results(self):
        q = np.argmin(self.pop_fit)
        return self.pop_dis[q], self.pop_pha[q], self.pop_amp[q]
        
    def evolve(self):
        # probabilities for cross over. To avoid calculationg random numbers every itteration.
        crossovers = np.random.uniform(size=(self.generations), low = 0, high=1)
        mutations = np.random.uniform(size=(self.generations), low = 0, high=1)
       
        index = 0;
        fittest = 0
        for i in range(self.generations):
            
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.ideal)
                self.pop_fit[dna] = score;
                if score < fittest:
                    fittest = score
                    index = dna
            
            self.pop_dis[0] = self.pop_dis[index]
            self.pop_pha[0] = self.pop_pha[index]
            self.pop_amp[0] = self.pop_amp[index]
             
            if i == self.generations-1:
                print('DONE')
                break
            
            if crossovers[i] < self.crossover_rate:
                # crossover occurs
                    s_1 = selection(self.pop_fit)
                    s_2 = selection(self.pop_fit)
                    
                    if False:
                        self.pop_dis[s_1] = (self.pop_dis[s_1] + self.pop_dis[s_2] )/2
                    elif True:
                        self.pop_pha[s_1] = (self.pop_pha[s_1] + self.pop_pha[s_2] )/2
                    elif False:
                        self.pop_amp[s_1] = (self.pop_amp[s_1] + self.pop_amp[s_2])/2
            
            if mutations[i] < self.mutation_rate:
                # mutation occurs
                s_1 = selection(self.pop_fit)
                if False:
                    self.pop_dis[s_1][np.random.randint(low=0, high=self.N-1)] =  np.random.uniform(low = LOW, high=HIGH)
                elif True:
                    self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
                elif False:
                    self.pop_amp[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=1)
        

if __name__ == "__main__":
    target = 45
    N = 6
    sims = 5

    best_d = np.zeros((sims, N-1), dtype=float)
    best_p = np.zeros((sims, N), dtype=float)
    best_a = np.zeros((sims, N), dtype=float)
   
    for i in range(sims):
        evo = Evolution(1000, 0.5, 0.1, 1000, N, target)
        dis, pha, amp = evo.results()
        best_d[i] = dis
        best_p[i] = pha
        best_a[i] = amp
        
    
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = fitness(best_d[i], best_p[i], best_a[i], target)
     
    # select fittest solution    
    q = np.argmin(fit)
    
    results(best_d, best_p, best_a, fit)
    
    # Display fittest solution
    show(best_d[q],  best_p[q],  best_a[q])
    #showUniform()
    plt.show()
    
    
    
        
    
