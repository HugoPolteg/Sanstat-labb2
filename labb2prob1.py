import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting
# Problem 1: Simulering av konfidensintervall
# Parametrar
# Antal mätningar
n = 1
# Väntevärdet
mu = 2
# Standardavvikelsen
sigma = 1
# Ett minus konfidensgraden
alpha = 0.05
# Antal intervall
m = 100
# Simulera n observationer för varje intervall.
medelvarians = []
medelutfall = []
for l in range(100):
    utfallen = []
    for k in range(100):
        x = stats.norm.rvs(loc=mu, scale=sigma, size=(m, n))
        # Skatta mu med medelvärdet.
        xbar = np.mean(x, axis=-1)
        # Beräkna kvantilerna och standardavvikelsen för
        # medelvärdet.
        lambda_alpha_2 = stats.norm.ppf(1 - alpha / 2)
        D = sigma / np.sqrt(n)
        # Beräkna undre och övre gränserna.
        undre = xbar - lambda_alpha_2 * D
        övre = xbar + lambda_alpha_2 * D
        ## Problem 1: Simulering av konfidensintervall (forts.)
        # Skapa en figur med storlek 4 × 8 tum.
        #plt.figure(figsize=(4, 8))
        # Rita upp alla intervall
        intervall_utanför = 0
        for k in range(m):
            # Rödmarkera alla intervall som missar mu.
            if övre[k] < mu or undre[k] > mu:
                color = 'r'
                intervall_utanför += 1
            else:
                color = 'b'
            #plt.plot([undre[k], övre[k]], [k, k], color)
        # Skriv ut antalet intervall som inte innehåller mu.
        utfallen.append(intervall_utanför)
        # Fixa till gränserna så att figuren ser lite bättre ut.
        b_min = np.min(undre)
        b_max = np.max(övre)
        #plt.axis([b_min, b_max, -1, m])
        # Rita ut det sanna värdet.
        #plt.plot([mu, mu], [-1, m], 'g')
        # Visa plotten.
    #plt.show()
    medelvarians.append(np.var(utfallen))
    medelutfall.append(np.mean(utfallen))
print(f'Varians: {np.mean(medelvarians)}')
print(f'Medelutfall: {np.mean(medelutfall)}')