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
   
        self.pop = np.ndarray(shape=(self.generations))
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
    
    def getfittest(self):
        return self.pop
        
    def evolve(self):
        # probabilities for cross over. To avoid calculationg random numbers every itteration.
        crossovers = np.random.uniform(size=(self.generations), low = 0, high=1)
        mutations = np.random.uniform(size=(self.generations), low = 0, high=1)
        
        for i in range(self.generations):
            tot = 0
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna], self.target)
                self.pop_fit[dna] = score;
                tot += score
            
            index = np.argmin(self.pop_fit)
            self.pop_pha[0] = self.pop_pha[index]
            self.pop_pha[-1] = self.pop_pha[index]
            
            tot = tot/self.population_tot
            self.pop[i] = self.pop_fit[index]
             
            if i == self.generations-1:
                print('DONE')
                break
            for _ in range(1):
                if crossovers[i] < self.crossover_rate:
                    # crossover occurs
                        s_1 = selection(self.pop_fit)
                        s_2 = selection(self.pop_fit)
                        self.pop_pha[s_1] = np.divide(self.pop_pha[s_1] + self.pop_pha[s_2],2)
                        #self.pop_pha[s_1][3:5] = (self.pop_pha[s_1][3:5] + self.pop_pha[s_2][3:5])/2
                        #self.pop_pha[s_2][0:2] = (self.pop_pha[s_1][0:2] + self.pop_pha[s_2][0:2])/2

                if mutations[i] < self.mutation_rate:
                    # mutation occurs
                    s_1 = selection(self.pop_fit)
                    self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
        


     
    

if __name__ == '__main__': 
    # ----
    #d = np.array([0.3,	0.475, 0.52, 0.475, 0.3]) 
    #d = np.array([0.425,	0.475,	0.5,	0.475, 0.425])
    d = np.array([0.35,	0.48,	0.56,	0.48, 0.35])
    #I = np.array([1, 1, 1, 1, 1, 1])
    #I = np.array([1, 5, 10, 10, 5, 1])
    I = np.array([0.32, 0.428, 0.54, 0.54, 0.428, 0.32])
    #I = np.array([0.098726072,	0.311798111,	0.688052999,	0.805729944,	0.536837113,	0.171841348])
    # 0.320600985	0.427582373	0.542381848	0,542381891	0,427582366	0,320600977




    target = 20
    N = 6;
    # Constants
    
    sims = 10
    best_p = np.zeros((sims, N), dtype=float)

    # Spacing and Phase
    for i in range(sims):
        evo = EvoPhase(5, 0.5, 1, 5000, N, d, target)
        pha = evo.results()
        best_p[i] = pha
    
        
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
    date_file = 'final_results2.xlsx'
    
    save_data(best_p, date_file, 'pha')
    # save_data(hpbw, date_file, 'hpbw')
    save_data(sll, date_file, 'sll')
    save_data(sll2, date_file, 'sll2')
    # save_data(directivity, date_file, 'dir')
    showUniform(target)
    show(d,  best_p[q],  I)
    
    plt.show()
    print(best_p)