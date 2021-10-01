import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import copy
from functions import *
from evophase import EvoPhase
from wexcel import *
date_file = 'found.xlsx'
spacings = read_data('find.xlsx')   

spacings = spacings.to_numpy()

d = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
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
i = 1
for d in spacings:
    
    sll = SLL(d, ph, am)
    hpbw = HPBW(d, ph, am)
    
    if sll < -8 and  hpbw <= 25:
        print(866-i)
        i+=1
        evo = EvoPhase(5, 0.5, 1, 3500, 6, d, 27)
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
            dir_20deg.append(getDirectivity(d,pha, am, 27))
            dir_90deg.append(getDirectivity(d,ph, am, 90))
            
save_data(spacing, date_file, 'spacing')
save_data(hpbw_90deg, date_file, 'hpbw_90deg')
save_data(hpbw_20deg, date_file, 'hpbw_20deg')
save_data(gl, date_file, 'gl')
save_data(gl2, date_file, 'gl2')
save_data(sll_90deg, date_file, 'sll_90deg')
save_data(sll_20deg, date_file, 'sll_20deg')
save_data(dir_90deg, date_file, 'dir_90deg')
save_data(dir_20deg, date_file, 'dir_20deg')