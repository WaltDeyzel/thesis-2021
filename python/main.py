from evophase import EvoPhase
from functions import *
import time
from wexcel import *
date_file = 'param.xlsx'

if __name__ == '__main__': 
    I = np.array([1, 1, 1, 1, 1, 1])
    d = np.array([0.5, 0.5, 0.5, 0.5, 0.5])


    target = 45
    
    # Constants
    gens = 1000
    sims = 3
   
    print('Start')
    par = np.zeros((sims, gens), dtype=float)
    # Spacing and Phase
    start = time.time()

    for i in range(sims):
        evo = EvoPhase(100, 0.5, 0.05, gens, 6, d, target)
        par[i] = evo.getParams()
       
    finish = time.time()   
    print('Time : ' , finish - start)
    #save_data(par.T, date_file, 'par10q00')
    showUniform(target)
    show(d,  evo.results(),  I)
    plt.show()
    plt.plot(par.T)
    plt.show()
    