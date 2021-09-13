import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from evolution import show, showUniform
# Average distance between the elements in the antenna array must be 2B. Which is 0.5
global theta
N = 6
# Constants
Beta = 2*np.pi
theta_deg = np.linspace(0, 180, 180)
theta = np.radians(theta_deg)

h = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
ph = np.array([0, 0, 0, 0, 0, 0])
am = np.array([1, 1, 1, 1, 1, 1])

target = 90
standard_deviation = 5

x_values = np.arange(0, 180, 1)
y_values = norm(target, standard_deviation) 
ideal = np.array(y_values.pdf(x_values))/np.max(np.array(y_values.pdf(x_values)))

def fitness(dd, alpha, I):
    Beta = 2*np.pi
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


#pop_dis = np.random.uniform(size=(population_tot, N-1), low = 0, high=1)
population_tot = 200;
err = 0.02
for i in range(population_tot):
    dna = np.random.uniform(size=(N-1), low = 0.1, high=1.3)
    avg = dna.mean()
    
    if avg < 0.5 + err and avg > 0.5 - err:
        print(avg)
        print(dna)
        print(fitness(dna, ph, am))
        print(fitness(h, ph, am))
        show(dna, ph, am)
        showUniform()
        plt.show()

