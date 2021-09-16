import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from scipy.stats import norm

def fitness(dd, alpha, I, target):

    f_ = AF(dd, alpha, I)
    return np.divide(np.square(np.sum(f_)), f_[target-1])

def selection(fitness):
    # fitness array
    r = np.random.randint(size = (2), low = 1, high = fitness.shape)
    if fitness[r[0]] < fitness[r[1]]:
        return r[0]
    else:
        return r[1]
    
def AF(dd, alpha, I):
    Beta = 2*np.pi
    theta_deg = np.linspace(0, 180, 180)
    theta = np.radians(theta_deg)
    d = np.zeros((alpha.shape), dtype=np.float)
    d[0] = 0
    for i in range(dd.shape[0]):
        d[i+1] = dd[i] + d[i]
    
    gamma = Beta * np.outer(np.cos(theta), d) + alpha[np.newaxis, :]
    return  np.abs(np.exp(1j*gamma) @ I) #/ 1.2589
     
    
def show(dd, alpha, I):
    
    f_ = AF(dd, alpha, I)
    print('deg', np.argmax(f_))
    theta_deg = np.linspace(0, 180, 180)
    f_ = 20*(np.log10(f_) -np.log10(np.max(f_)))
    plt.plot(theta_deg, f_)
    plt.ylim([-30, 0])
    plt.title('AF')
    plt.xlabel("theta (degrees)")
    plt.ylabel("Normalized Magnitude")
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
    
def results(best_d, best_p, best_a, fit):
    # select fittest solution    
    q = np.argmin(fit)
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
    
    print()
    print('fitAll', np.round(fit,5))
    print('fit', np.min(fit))            
    print('info')         
    print('dis', np.round(best_d[q],2))
    print('pha', np.round(best_p[q]*180/np.pi,2))
    print('amp', np.round(best_a[q],2))
    
    
def HPBW(dd, alpha, I):
    f_ = np.log10(AF(dd, alpha, I))*20
    
    dir = np.argmax(f_)
    gain = f_[dir-1]
    point = f_[dir-1]
    i = 0
    while point > gain - 3 and (i + dir < 180):
        point = f_[dir-1 + i]
        i += 1
    point = f_[dir-1]   
    a = 0 
    while point > gain - 3  and (dir  - a > 0):
        point = f_[dir-1 - a]
        a += 1
    
    
    hpbw = i + a 
    
    return hpbw

def SLL(dd, alpha, I):
    
    f_ = AF(dd, alpha, I)
    
    main_beam = 0
    sll = 0
    
    if f_[0] > f_[-1]:
        main_beam = f_[0]
        sll = f_[-1]
    elif f_[-1] > f_[0]:
        main_beam = f_[-1]
        sll = f_[0]
    
    for i in range(1, len(f_)-1):
        
        if((f_[i] > f_[i-1] and f_[i] > f_[i+1]) or (f_[i] > f_[i-1] and f_[i] == f_[i+1])):
            #peak
            print(f_[i])
            if f_[i] > sll and f_[i] < main_beam:
                sll = f_[i]
            elif f_[i] > main_beam:
                sll = main_beam
                main_beam = f_[i] 
    
    return 20*np.log10(sll) - 20*np.log10(np.max(f_))
    
