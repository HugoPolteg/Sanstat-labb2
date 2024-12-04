import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting
## Problem 2: Maximum likelihood, minsta kvadrat
M = 10000
b = 4
# Simulera M utfall med parameter b.
x = stats.rayleigh.rvs(scale=b, size=M)
# Skapa figur och plotta histogrammet.
plt.figure()
plt.hist(x, 40, density=True)
est_ml = np.sqrt(np.mean(x**2)/2)
est_mk = np.mean(x)*np.sqrt(2/np.pi)

# Beräkna felen
error_ml = abs(est_ml - b)
error_mk = abs(est_mk - b)

# Skriv ut felen i konsolen
print(f"Fel för ML: {error_ml}")
print(f"Fel för MK: {error_mk}")

# Plotta de två skattningarna.
plt.plot(est_ml, 0.2, 'r*', markersize=10)
plt.plot(est_mk, 0.2, 'g*', markersize=10)
plt.plot(b, 0.2, 'bo')
plt.show()
## Problem 2: Maximum likelihood, minsta kvadrat (forts.)
# Skapa figur.
plt.figure()
# Visa histogrammet.
plt.hist(x, 40, density=True)
# Plotta täthetsfunktionen för den skattade parametern.
x_grid = np.linspace(np.min(x), np.max(x), 60)
pdf = stats.rayleigh.pdf(x_grid, scale=est_ml)
plt.plot(x_grid, pdf, 'r')
plt.show()