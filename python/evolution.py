import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

from functions import *

from evophase import *

global LOW, HIGH
LOW = 0.1
HIGH = 1

class Evolution:
    
    def __init__(self, population_tot, crossover_rate, mutation_rate, generations, N, target, settings):
        self.population_tot = population_tot
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.N = N
        self.target = target
        self.settings = settings
        
        # Spacing between 
        #self.pop_dis = np.random.uniform(size=(self.population_tot, self.N-1), low = LOW, high=HIGH)
        #self.pop_dis = np.array([[0.5, 0.5, 0.5, 0.5, 0.5],[1., 1., 1., 1., 1.], [2., 2., 2., 2., 2.]])
        self.pop_dis = np.ndarray(shape=(self.population_tot, self.N-1))
        
        for i in range(self.population_tot):
            a = np.random.uniform(low = LOW, high=HIGH)
            b = np.random.uniform(low = LOW, high=HIGH)
            self.pop_dis[i][4] = a;
            self.pop_dis[i][0] = a
            self.pop_dis[i][1] = b
            self.pop_dis[i][3] = b
            
            self.pop_dis[i][2] = np.random.uniform(low = LOW, high=HIGH)
       
        # Phase Shift
        self.pop_pha = np.random.uniform(size = (self.population_tot, self.N), low = 0, high = 2*np.pi) # randians
        
        # Amplitude 
        self.pop_amp = np.random.uniform(size=(self.population_tot, self.N), low = 0, high=1)
        
        # Fitness
        self.pop_fit = np.zeros(self.population_tot, dtype = np.float)
        
        self.evolve()
    
    def results(self):
        q = np.argmin(self.pop_fit)
        return self.pop_dis[q], self.pop_pha[q], self.pop_amp[q]
        
    def evolve(self):
        # probabilities for cross over. To avoid calculationg random numbers every itteration.
        crossovers = np.random.uniform(size=(self.generations), low = 0, high=1)
        mutations = np.random.uniform(size=(self.generations), low = 0, high=1)
        # Probabilities for which parameter to mutate or to do crossover
        choice = np.random.uniform(size=(self.generations), low = 0, high=1)
        
        
        for i in range(self.generations):
            index = 0;
            fittest = 0
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.target)
                self.pop_fit[dna] = score;
                if score < fittest:
                    # evo = EvoPhase(1000, 0.5, 0.05, 1000, self.N, self.pop_dis[dna], self.target)
                    # self.pop_pha[dna] = evo.results()
                    fittest = score
                    index = dna
            
            self.pop_dis[0] = self.pop_dis[index]
            self.pop_pha[0] = self.pop_pha[index]
            self.pop_amp[0] = self.pop_amp[index]
             
            if i == self.generations-1:
                print('Gen', i)
                break
            
            if crossovers[i] < self.crossover_rate:
                # crossover occurs
                    s_1 = selection(self.pop_fit)
                    s_2 = selection(self.pop_fit)
                    
                    if choice[i] <= 0.5 and self.settings[0]:
                        self.pop_dis[s_1] = (self.pop_dis[s_1] + self.pop_dis[s_2] )/2
                    elif choice[i] > 0.5 and self.settings[1]:
                        self.pop_pha[s_1] = (self.pop_pha[s_1] + self.pop_pha[s_2] )/2
                    #elif choice[i] > 0.66 and self.settings[2]:
                    self.pop_amp[s_1] = (self.pop_amp[s_1] + self.pop_amp[s_2])/2
            
            if mutations[i] < self.mutation_rate:
                # mutation occurs
                s_1 = selection(self.pop_fit)
                if choice[-i] <= 0.5 and self.settings[0]:
                    rs = np.random.uniform(low = LOW, high=HIGH)
                    a = np.random.randint(low=0, high=self.N-1)
                    # SYMETRICAL SPACING 
                    self.pop_dis[s_1][a] =  rs
                    self.pop_dis[s_1][(self.N-2 - a)] =  rs
                    
                elif choice[-i] > 0.5 and self.settings[1]:
                    #self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
                    # OPTIMIZE PHASE HERE
                    evo = EvoPhase(50, 0.5, 0.05, 1000, N, self.pop_dis[s_1], target)
                    self.pop_pha[s_1] = evo.results()

                if choice[-i] > 0.5 and self.settings[2]:
                    self.pop_amp[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=3)
        


if __name__ == "__main__":
    
    target = 60
    N = 6;
    # Constants
    
    sims = 1
    best_d = np.zeros((sims, N-1), dtype=float)
    best_p = np.zeros((sims, N), dtype=float)
    best_a = np.zeros((sims, N), dtype=float)
    # Spacing and Phase
    settings = np.array([True, True, True], dtype=bool);
    for i in range(sims):
        evo = Evolution(1000, 0.5, 0.1, 500, N, target, settings)
        dis, pha, amp = evo.results()
        best_d[i] = dis
        best_p[i] = pha
        best_a[i] = amp
  
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = fitness(best_d[i], best_p[i], best_a[i], target)
     
    results(best_d, best_p, best_a, fit)
    # Display fittest solution
    # select fittest solution    
    q = np.argmin(fit)
    
    show(best_d[q],  best_p[q],  best_a[q])
    #showUniform()
    plt.show()
    from wexcel import *
    # save_data([best_d[q],  best_p[q],  best_a[q], fit[q]], 'Data.xlsx', 'spacing', 10)
    # save_data(np.round(best_d[q],3), 'Data.xlsx', 'spacing', 10)
    # save_data(np.round(best_p[q]*180/np.pi,2), 'Data.xlsx', 'phase', 10)
    # save_data(np.round(best_a[q],2), 'Data.xlsx', 'amp', 10)

    
    