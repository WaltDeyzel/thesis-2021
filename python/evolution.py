import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import normalize

global LOW, HIGH
LOW = 0.25
HIGH = 1.4

class Evolution:
    
    def __init__(self, population_tot, crossover_rate, mutation_rate, generations, N):
        self.population_tot = population_tot
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.N = N
        
        # Spacing between 
        self.pop_dis = np.random.uniform(size=(self.population_tot, self.N-1), low = LOW, high=HIGH)
        #self.pop_dis = np.array([[0.5, 0.5, 0.5, 0.5, 0.5],[1., 1., 1., 1., 1.], [2., 2., 2., 2., 2.]])
       
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
        index = 0;
        fittest = 0
        for i in range(self.generations):
            
            for dna in range(self.population_tot):
                score = fitness(self.pop_dis[dna], self.pop_pha[dna], self.pop_amp[dna])
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
                    
                    if choice[i] <= 0.33:
                        self.pop_dis[s_1] = (self.pop_dis[s_1] + self.pop_dis[s_2] )/2
                    elif choice[i] > 0.33 and choice[i] <= 0.66:
                        self.pop_pha[s_1] = (self.pop_pha[s_1] + self.pop_pha[s_2] )/2
                    elif choice[i] > 0.66:
                        self.pop_amp[s_1] = (self.pop_amp[s_1] + self.pop_amp[s_2])/2
            
            if mutations[i] < self.mutation_rate:
                # mutation occurs
                s_1 = selection(self.pop_fit)
                if choice[-i] <= 0.33:
                    self.pop_dis[s_1][np.random.randint(low=0, high=self.N-1)] =  np.random.uniform(low = LOW, high=HIGH)
                elif choice[-i] > 0.33 and choice[-i] <= 0.66:
                    self.pop_pha[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=2*np.pi)
                elif choice[-i] > 0.66:
                    self.pop_amp[s_1][np.random.randint(low=0, high=self.N)] =  np.random.uniform(low = 0, high=3)
        

def fitness(dd, alpha, I):
    
    d = np.zeros((alpha.shape), dtype=np.float)
    d[0] = 0
    for i in range(dd.shape[0]):
        d[i+1] = dd[i] + d[i]
    
    gamma = Beta * np.outer(np.cos(theta), d) + alpha[np.newaxis, :]
    f_abs_ = np.abs(np.exp(1j*gamma) @ I) #/ 1.2589
    f_ = np.divide(f_abs_, np.max(f_abs_))
    
    # print(np.square(np.subtract(ideal, f_)).mean())
    # plt.plot(f_)
    # plt.plot(ideal)
    # plt.plot(np.square(np.subtract(ideal, f_)))
    # plt.show()
    return np.sum(np.square(np.subtract(ideal, f_)))
    #q = 5 
    #sum1 = (np.sum(f_[target-q+1:target+q])) # main beam
    # sum2 = (np.sum(f_[0:target-q]) + np.sum(f_[target+q+1:])) # outside main beam
    # directivity = sum1 / sum2
    # return -directivity   
        

def selection(fitness):
    # fitness array
    r = np.random.randint(size = (2), low = 1, high = fitness.shape)
    if fitness[r[0]] < fitness[r[1]]:
        return r[0]
    else:
        return r[1]
    
def show(dd, alpha, I):
    d = np.zeros(alpha.shape, dtype=np.float)
    d[0] = 0
    for i in range(dd.shape[0]):
        d[i+1] = dd[i] + d[i]

    gamma = Beta * np.outer(np.cos(theta), d) + alpha[np.newaxis, :]
    f_ = np.exp(1j*gamma) @ I

    f_abs_ =20*np.log(np.abs(f_)) /2 
    
    f_ =  np.round(f_abs_-np.max(f_abs_),1)
   
    print('deg', np.argmax(f_))

    plt.plot(theta_deg, f_)
    plt.ylim([-30, 0])
    
    plt.xlabel("theta (degrees)")
    plt.ylabel("f(theta)")
    #plt.show()

def showUniform():
    d = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
    ph = np.array([0, 0, 0, 0, 0, 0])
    am = np.array([1, 1, 1, 1, 1, 1])
    show(d, ph, am)
    d = np.array([1, 1, 1, 1, 1])
    show(d, ph, am)
    
def showAll(spacing, alpha, amplitude, fitness):
    for i in range(alpha.shape[0]):
        print(fitness[i])
        show(spacing[i], alpha[i], amplitude[i])
    


if __name__ == "__main__":
    
    target = 60
    standard_deviation = 5

    x_values = np.arange(0, 180, 1)
    y_values = norm(target, standard_deviation) 
    ideal = np.array(y_values.pdf(x_values))/np.max(np.array(y_values.pdf(x_values)))
    print(type(ideal))
    plt.plot(x_values, ideal)
    
    plt.show()
    
    N = 6;
    # Constants
    Beta = 2*np.pi
    theta_deg = np.linspace(0, 180, 180)
    theta = np.radians(theta_deg)
    
    sims = 10
    best_d = np.zeros((sims, N-1), dtype=float)
    best_p = np.zeros((sims, N), dtype=float)
    best_a = np.zeros((sims, N), dtype=float)
   
    for i in range(sims):
        evo = Evolution(1000, 0.5, 0.25, 1000, N)
        dis, pha, amp = evo.results()
        best_d[i] = dis
        best_p[i] = pha
        best_a[i] = amp
        
    print('RESULTS')
    print()
    print('Best_d')
    print(best_d)
    print('Var')
    print(np.round(np.var(best_d, axis=0),3))
    print()
    
    print('Best_p')
    #print(best_p*180/np.pi)
    print('Var')
    print(np.round(np.var(best_p, axis=0),3))
    print()
    
    print('Best_a')
    #print(best_a)
    print('Var')
    print(np.round(np.var(best_a, axis=0),3))
    print()
    
    # Recalculate all fitness scores
    fit = np.zeros((sims), dtype=float)
    for i in range(sims):
        fit[i] = fitness(best_d[i], best_p[i], best_a[i])
     
    # select fittest solution    
    q = np.argmin(fit)
    
    
    print()
    print('fitAll', np.round(fit,5))
    print('fit', np.min(fit))            
    print('info')         
    print('dis', np.round(best_d[q],2))
    print('pha', np.round(best_p[q]*180/np.pi,2))
    print('amp', np.round(best_a[q],2))
    
    # Display fittest solution
    show(best_d[q],  best_p[q],  best_a[q])
    #showUniform()
    plt.show()
    
    