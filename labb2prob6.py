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
alpha = 0.05
n_x = len(x)
n_y = len(y)
v_x = np.var(x)
v_y = np.var(y)
d = np.sqrt(v_x/n_x + v_y/n_y)
t_alpha = stats.t.ppf(1-alpha/2, n_x + n_y - 2)
print(f't_alpha: {t_alpha}')
print(f'd: {d}')
lower_bound = res - t_alpha*d
upper_bound = res + t_alpha*d
print(f'Konfidensintervallet är [{lower_bound}, {upper_bound}] kring {res} med konfidensgrad {(1-alpha)*100}%.')
