from evoamp import EvoAmp
from functions import *
#d = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
# ----
d = np.array([0.3,	0.475, 0.52, 0.475, 0.3]) 
d1 = np.array([0.425,	0.475,	0.5,	0.475, 0.425])
d2 = np.array([0.35,	0.48,	0.56,	0.48, 0.35])

p = np.array([0, 0, 0, 0, 0, 0])

#p = np.array([])
target = 90
N = 6;
# Constants

sims = 1
best_a = np.zeros((sims, N), dtype=float)

# Spacing and Phase
for i in range(sims):
    evo = EvoAmp(5, 0, 1, 10000, N, d, target)
    amp = evo.results()
    best_a[i] = amp
    
# Recalculate all fitness scores
fit = np.zeros((sims), dtype=float)
hpbw = np.zeros((sims), dtype=float)
sll = np.zeros((sims), dtype=float)
for i in range(sims):
    fit[i] = SLL(d, p, best_a[i])
    hpbw[i] = HPBW(d, p, best_a[i])
    sll[i] = SLL(d, p, best_a[i])
    

# select fittest solution    
q = np.argmin(fit)

print('RESULTS')
print(best_a[q])
print(best_a)
#show(d,  p, np.array([1, 1, 1, 1, 1, 1]))
showUniform(33)
show(d,  p, best_a[q])


from wexcel import *
date_file = 'amp_6.xlsx'

# save_data(best_a, date_file, 'amp')
# #save_data([HPBW(d, p, best_a[q]), SLL(d, p, best_a[q])], date_file, 'hpbw')
# save_data(fit, date_file, 'fit')
# save_data(hpbw, date_file, 'hpbw')
# save_data(sll, date_file, 'sll')


print('SLL', SLL(d, p, best_a[q]))
print('HPBW',HPBW(d, p, best_a[q]))
plt.show()