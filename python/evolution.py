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
        self.pop_amp = np.random.uniform(size=(self.population_tot, self.N), low = 1, high=1)
        
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

            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.target)
                self.pop_fit[dna] = score;
            
            index = np.argmin(self.pop_fit)
            self.pop_dis[0] = self.pop_dis[index]
            self.pop_pha[0] = self.pop_pha[index]
            self.pop_dis[-1] = self.pop_dis[index]
            self.pop_pha[-1] = self.pop_pha[index]
            #self.pop_amp[0] = self.pop_amp[index]
            
            evo = EvoPhase(5, 0.5, 1, 2000, self.N, self.pop_dis[0], self.target)
            self.pop_pha[0] = evo.results()
             
            if i == self.generations-1:
                print('Gen', i)
                break
            for _ in range(1):
                if crossovers[i] < self.crossover_rate:
                    # crossover occurs
                        s_1 = selection(self.pop_fit)
                        s_2 = selection(self.pop_fit)
                        
                        if choice[i] <= 0.5 and self.settings[0]:
                            self.pop_dis[s_1] = (self.pop_dis[s_1] + self.pop_dis[s_2] )/2
                        elif choice[i] > 0.5 and self.settings[1]:
                            self.pop_pha[s_1] = (self.pop_pha[s_1] + self.pop_pha[s_2] )/2
                
                if mutations[i] < self.mutation_rate:
                    # mutation occurs
                    s_1 = selection(self.pop_fit)
                    if choice[-i] <= 0.5 and self.settings[0]:
                        rs = np.random.uniform(low = LOW, high=HIGH)
                        a = np.random.randint(low=0, high=self.N-1)
                        # SYMETRICAL SPACING 
                        self.pop_dis[s_1][a] =  rs
                        #self.pop_dis[s_1][(self.N-2 - a)] =  rs
                        
                    elif choice[-i] > 0.5 and self.settings[1]:
                        self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
                        # OPTIMIZE PHASE HERE

        
        


if __name__ == "__main__":
    
    target = 90
    N = 6;
    # Constants
    
    sims = 1
    best_d = np.zeros((sims, N-1), dtype=float)
    best_p = np.zeros((sims, N), dtype=float)
    best_a = np.zeros((sims, N), dtype=float)
    hpbw = np.zeros((sims), dtype=float)
    sll = np.zeros((sims), dtype=float)
    # Spacing and Phase
    settings = np.array([True, True, True], dtype=bool);
    for i in range(sims):
        evo = Evolution(25, 0.5, 1, 500, N, target, settings)
        dis, pha, amp = evo.results()
        best_d[i] = dis
        best_p[i] = pha
        best_a[i] = amp
        hpbw[i] = HPBW(best_d[i], best_p[i], best_a[i])
        sll[i] = SLL(best_d[i], best_p[i], best_a[i])
  
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = fitness(best_d[i], best_p[i], best_a[i], target)
     
    # Display fittest solution
    # select fittest solution    
    q = np.argmin(sll)
    
    from wexcel import *
    date_file = '0deg.xlsx'
    
    save_data(best_d, date_file, 'spa')
    save_data(best_p, date_file, 'pha')
    save_data(best_a, date_file, 'amp')
    save_data(fit, date_file, 'fit')
    save_data(hpbw, date_file, 'hpbw')
    save_data(sll, date_file, 'sll')
    
    showUniform(target)
    show(best_d[q],  best_p[q],  best_a[q])
    plt.show()
    

    
    