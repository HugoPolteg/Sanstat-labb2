import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting
## Problem 3: Konfidensintervall for Rayleighfordelning
# Ladda data.
y = np.loadtxt('wave_data.dat')
# Plotta en bit av signalen samt histogrammet.
plt.figure(figsize=(4, 8))
plt.subplot(2, 1, 1)
plt.plot(y[:100])
plt.subplot(2, 1, 2)
plt.hist(y, density=True)
plt.show()
est = np.mean(y)*np.sqrt(2/np.pi)
# Beräkna konfidensintervallet.
alpha = 0.05
n = len(y)
lambda_alpha_2 = stats.norm.ppf(1 - alpha / 2)
d = est*np.sqrt((4-np.pi)/(n*np.pi))
lower_bound = est - d*lambda_alpha_2
upper_bound = est + d*lambda_alpha_2
print(f'Konfidensintervallet är [{lower_bound}, {upper_bound}] kring {est} med konfidensgrad {(1-alpha)*100}%.')
n = len(y)
## Problem 3: Konfidensintervall (forts.)
# Plotta histogrammet och skattningen.
plt.figure()
plt.hist(y, density=True)
plt.plot(lower_bound, 0.6, 'g*', markersize=10)
plt.plot(upper_bound, 0.6, 'g*', markersize=10)
# Plotta täthetsfunktionen med den skattade parametern.
x_grid = np.linspace(np.min(y), np.max(y), 60)
pdf = stats.rayleigh.pdf(x_grid, scale=est)
plt.plot(x_grid, pdf, 'r')
plt.show()