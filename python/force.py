import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import copy
from functions import *
from evophase import EvoPhase
# Average distance between the elements in the antenna array must be 2B. Which is 0.5
from wexcel import *
date_file = 'force.xlsx'
   
    

d = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
ph = np.array([0, 0, 0, 0, 0, 0])
am = np.array([1, 1, 1, 1, 1, 1])

dd = []
sll = []
hpbw = []

best_score = 1000;
q = 0.1
limit = 1.5
while True:
    
    if SLL(d, ph, am) < -5:
            
        evo = EvoPhase(5, 0.5, 1, 5000, 6, d, 20)
        pha = evo.results()
        score = SLL(d, pha, am)
        
        if score < best_score and SLL2(d, pha, am) < -3:
            best_score = score
            dd.append(copy(d))
            sll.append(SLL(d, pha, am))
            hpbw.append(HPBW(d,pha, am))
            #print('score',score, 'dna', d)
            # showUniform(20)
            # show(d, pha, am)
            # plt.show()
    print(d)
    d[4] += q
    d[0] += q
    
    if d[4] > limit:
        d[4] = 0.1
        d[0] = 0.1
        
        d[3] += q
        d[1] += q
        
        if d[3] > limit:
            d[3] = 0.1
            d[1] = 0.1
            
            d[2] += q 
            
            if d[2] > limit:
                print('END')
                break
            
            
            
         
    # NOT SYMETRIC
    # d[4] += q
    # if d[4] > limit:
    #     d[4] = 0.1
    #     d[3] += q
    #     if d[3] > limit:
    #         d[3] = 0.1
    #         d[2] += q
    #         if d[2] > limit:
    #             d[2] = 0.1
    #             d[1] += q
    #             if d[1] > limit:
    #                 d[1] = 0.1
    #                 d[0] += q
    #                 if d[0] >= limit:
    #                     break

save_data(dd, date_file, 'spa')
save_data(hpbw, date_file, 'hpbw')
save_data(sll, date_file, 'sll')