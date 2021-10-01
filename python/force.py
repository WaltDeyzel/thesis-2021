import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import copy
from functions import *
from evophase import EvoPhase
# Average distance between the elements in the antenna array must be 2B. Which is 0.5
from wexcel import *
date_file = 'force_uniform.xlsx'
   
    

d = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
ph = np.array([0, 0, 0, 0, 0, 0])
am = np.array([1, 1, 1, 1, 1, 1])

spacing = []
hpbw_90deg = []
hpbw_20deg = []
sll_90deg = []
sll_20deg = []
gl = []

dir_90deg = []
dir_20deg = []

best_score = 1000;
q = 0.01
limit = 1.025
while True:
    
    sll = SLL(d, ph, am)
    hpbw = HPBW(d, ph, am)
    
    # if sll < -4 and  hpbw <= 26:
            
    #     evo = EvoPhase(5, 0.5, 1, 5000, 6, d, 20)
    #     pha = evo.results()
    #     grating = SLL(d, pha, am)
    #     sll2 = SLL2(d, pha, am) 
        
    #     if sll2 < -3:
    spacing.append(copy(d))
    #gl.append(grating) 
    #sll_20deg.append(sll2)
    sll_90deg.append(sll)
    #hpbw_20deg.append(HPBW(d,pha, am))
    hpbw_90deg.append(hpbw)
    
    #dir_20deg.append(getDirectivity(d,pha, am, 20))
    dir_90deg.append(getDirectivity(d,ph, am, 90))
    #         #print('score',score, 'dna', d)
    #         # showUniform(20)
    #         # show(d, pha, am)
    #         # plt.show()
            
    print(d)
    d[0] += q
    d[1] += q
    d[2] += q
    d[3] += q
    d[4] += q
    
    if d[2] > 2.1:
        break
    # d[4] += q
    # d[0] += q
    
    # if d[4] > limit:
    #     d[4] = 0.1
    #     d[0] = 0.1
        
    #     d[3] += q
    #     d[1] += q
        
    #     if d[3] > limit:

    #         d[3] = 0.1
    #         d[1] = 0.1
            
    #         d[2] += q 
            
    #         if d[2] > limit:
    #             print('END')
    #             break
  
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

save_data(spacing, date_file, 'spacing')
save_data(hpbw_90deg, date_file, 'hpbw_90deg')
save_data(hpbw_20deg, date_file, 'hpbw_20deg')
save_data(gl, date_file, 'gl')
save_data(sll_90deg, date_file, 'sll_90deg')
save_data(sll_20deg, date_file, 'sll_20deg')
save_data(dir_90deg, date_file, 'dir_90deg')
save_data(dir_20deg, date_file, 'dir_20deg')