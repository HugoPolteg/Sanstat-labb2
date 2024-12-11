import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting

#Ladda data
birth = np.loadtxt('birth.dat')

#Extrahera rökare och icke rökare
smokers = (birth[:, 19] == 3)
non_smokers = (birth[:, 19] < 3)
# Extrahera födelsevikten (kolonn 3) för de två kategorierna.
x = birth[smokers, 2]
y = birth[non_smokers, 2]
#Jämför skillnaden i födelsevikt mellan rökare och icke rökare
res = np.mean(y) - np.mean(x)
print(f'Skillnaden i väntevärdet för födelsevikt mellan rökare och icke rökare är {res} gram')
#Hitta konfidensintervallet för skillnaden


def stickprovsstandardavvikelse(x):
    summa = 0
    for element in x:
        summa += (element - np.mean(x))**2
    return np.sqrt(summa/(len(x)-1))

alpha = 0.05
n_x = len(x)
n_y = len(y)
# eftersom n är stort kan vi skatta variansen med stickprovsvariansen
v_x = stickprovsstandardavvikelse(x)**2 
v_y = stickprovsstandardavvikelse(y)**2



d = np.sqrt(v_x/n_x + v_y/n_y)
t_alpha = stats.t.ppf(1-alpha/2, n_x + n_y - 2)
lambda_alpha = stats.norm.ppf(1-alpha/2)
print(f't_alpha: {t_alpha}')
print(f'lambda_alpha: {lambda_alpha}')
print(f'd: {d}')

lower_bound = res - t_alpha*d
upper_bound = res + t_alpha*d

lower_bound_lambda = res - lambda_alpha*d
upper_bound_lambda = res + lambda_alpha*d

print("för t:")
print(f'Konfidensintervallet är [{lower_bound}, {upper_bound}] kring {res} med konfidensgrad {(1-alpha)*100}%.')
print("för lambda:")
print(f'Konfidensintervallet är [{lower_bound_lambda}, {upper_bound_lambda}] kring {res} med konfidensgrad {(1-alpha)*100}%.')
