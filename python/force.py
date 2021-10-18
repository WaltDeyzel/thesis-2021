import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import copy
from functions import *
from evophase import EvoPhase
from wexcel import *
date_file = 'random.xlsx'
# spacings = read_data('find.xlsx')   

# spacings = spacings.to_numpy()
start = 0.3
d = np.array([0.55, 0.55, 0.55, 0.55, 0.3])
ph = np.array([0, 0, 0, 0, 0, 0])
am = np.array([1, 1, 1, 1, 1, 1])

spacing = []
hpbw_90deg = []
hpbw_20deg = []
sll_90deg = []
sll_20deg = []
gl = []
gl2 = []

dir_90deg = []
dir_20deg = []
while True:
    
    sll = SLL(d, ph, am)
    hpbw = HPBW(d, ph, am)
    
    if sll < -10 and  hpbw <= 22:

        evo = EvoPhase(5, 0, 1, 3500, 6, d, 30)
        pha = evo.results()
        sll2 = SLL2(d, pha, am) 
        
        if sll2 < -3:
            af = AF(d, pha, am)
            spacing.append(copy(d))
            gl.append(af[0]) 
            gl2.append(af[-1]) 
            sll_20deg.append(sll2)
            sll_90deg.append(sll)
            hpbw_20deg.append(HPBW(d,pha, am))
            hpbw_90deg.append(hpbw)
            dir_20deg.append(getDirectivity(d,pha, am, 30))
            dir_90deg.append(getDirectivity(d,ph, am, 90))
    
    print(d)
    q = 0.025
    d[0] += q
    
    if d[4] >=  0.55 and d[3] >=  0.55 and d[2] >=  0.55 and d[1] >=  0.55 and d[0] >= 0.55:
        break
    
    if d[0] >=  0.55:
        d[0] = start
        d[1] += q
        if d[1] >=  0.55:
            d[1] = start
            d[2] += q
            if d[2] >=  0.55:
                d[2] = start
                d[3] += q
                if d[3] >=  0.55:
                    d[3] = start
                    d[4] += q
    
    
            
                    save_data(spacing, date_file, 'spacing')
                    save_data(hpbw_90deg, date_file, 'hpbw_90deg')
                    save_data(hpbw_20deg, date_file, 'hpbw_20deg')
                    save_data(gl, date_file, 'gl')
                    save_data(gl2, date_file, 'gl2')
                    save_data(sll_90deg, date_file, 'sll_90deg')
                    save_data(sll_20deg, date_file, 'sll_20deg')
                    save_data(dir_90deg, date_file, 'dir_90deg')
                    save_data(dir_20deg, date_file, 'dir_20deg')
                    
                    spacing = []
                    hpbw_90deg = []
                    hpbw_20deg = []
                    sll_90deg = []
                    sll_20deg = []
                    gl = []
                    gl2 = []

                    dir_90deg = []
                    dir_20deg = []