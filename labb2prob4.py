import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting

## Problem 4: Fördelningar av givna data
# Ladda datafilen.
birth = np.loadtxt('birth.dat')
# Definiera filter beroende på om modern röker (kolonn 20
# är 3) eller inte (kolonn 20 är 1 eller 2). Notera att
# eftersom indexering i Python börjar med noll så betecknas
# kolonn 20 med indexet 19.
non_smokers = (birth[:, 19] < 3)
smokers = (birth[:, 19] == 3)
# Extrahera födelsevikten (kolonn 3) för de två kategorierna.
x = birth[non_smokers, 2]
y = birth[smokers, 2]

print(np.shape(x), np.shape(y))


## Problem 4: Fördelningar av givna data (forts.)
# Skapa en stor figur.
plt.figure(figsize=(8, 8))
# Plotta ett låddiagram över x.
plt.subplot(2, 2, 1)
plt.boxplot(x)
plt.axis([0, 2, 500, 5000])
plt.title('Födelsevikt för icke-rökande mödrar')
# Plotta ett låddiagram över y.
plt.subplot(2, 2, 2)
plt.boxplot(y)
plt.axis([0, 2, 500, 5000])
plt.title('Födelsevikt för rökande mödrar')
# Beräkna kärnestimator för x och y. Funktionen
# gaussian_kde returnerar ett funktionsobjekt som sedan
# kan evalueras i godtyckliga punkter.
kde_x = stats.gaussian_kde(x)
kde_y = stats.gaussian_kde(y)
# Skapa ett rutnät för vikterna som vi kan använda för att
# beräkna kärnestimatorernas värden.
min_val = np.min(birth[:, 2])
max_val = np.max(birth[:, 2])
grid = np.linspace(min_val, max_val, 60)
# Plotta kärnestimatorerna.
plt.subplot(2, 2, (3, 4))
plt.plot(grid, kde_x(grid), 'b')
plt.plot(grid, kde_y(grid), 'r')

plt.legend(['Icke-rökare', 'Rökare'])

plt.show()

# Utvärdering av skillnaden mellan kön i födelsevikt

non_training = (birth[:, 24] < 3)
training = (birth[:, 24] == 3)
x = birth[training, 2]
y = birth[non_training, 2]
x = x[~np.isnan(x)]
y = y[~np.isnan(y)]
print(np.shape(x), np.shape(y))
plt.figure(figsize=(8, 8))
# Plotta ett låddiagram över x.
plt.subplot(2, 2, 1)
plt.boxplot(x)
plt.axis([0, 2, 500, 5000])
plt.title('Födelsevikt för tränande') 
# Plotta ett låddiagram över y.
plt.subplot(2, 2, 2)
plt.boxplot(y)
plt.axis([0, 2, 500, 5000])
plt.title('Födelsevikt för icke-tränande')

kde_x = stats.gaussian_kde(x)
kde_y = stats.gaussian_kde(y)

min_val = np.min(birth[:, 2])
max_val = np.max(birth[:, 2])
grid = np.linspace(min_val, max_val, 60)
# Plotta kärnestimatorerna.
plt.subplot(2, 2, (3, 4))
plt.plot(grid, kde_x(grid), 'b')
plt.plot(grid, kde_y(grid), 'r')

plt.legend(['tränande', 'icke-tränande'])

plt.show()