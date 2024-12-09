import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting

#Ladda data
moore = np.loadtxt('moore.dat')
år = moore[:, 0]
antal_resistorer = moore[:, 1]
w = np.log(antal_resistorer)

X  = np.ones((len(år), 2))
X[:, 1] = år
#Beräkna linjär regression
beta_hat, beta_interval = tools.regress(X, w)
print(beta_hat)
beta_hat = np.array(beta_hat)
#Plotta data och linjär regression
plt.figure()
plt.scatter(år, np.log(antal_resistorer))
plt.plot(år, X @ beta_hat, 'r')
plt.xlabel('År')
plt.ylabel('Antal transistorer')
plt.legend(['Data', 'Linjär regression'])
plt.title('Logaritmerad data och linjär regression')
plt.show()


print(np.shape(X))
print(np.shape(beta_hat))
## Problem 6: Regression
# Bilda residualerna.
res = w - X @ beta_hat
# Skapa figur.
plt.figure(figsize=(4, 8))
# Plotta kvantil–kvantil-plot för residualerna.
plt.subplot(2, 1, 1)
_ = stats.probplot(res, plot=plt)
# Plotta histogram för residualerna.
plt.subplot(2, 1, 2)
plt.hist(res, density=True, bins=30)
# Plotta täthetsfunktionen för residualerna.
x_grid = np.linspace(np.min(res), np.max(res), 60)
pdf = stats.norm.pdf(x_grid, loc=np.mean(res), scale=np.std(res))
plt.plot(x_grid, pdf, 'r')
plt.show()

Q0 = np.sum(res**2)
s = np.sqrt(Q0/(len(år)-2))
print(f'Standardavvikelsen för residualerna kan skattas till {s}')

_, res_p = stats.jarque_bera(res)
if(res_p < 0.05):
    print('Residualerna är inte normalfördelade')
else:
    print('Residualerna är normalfördelade')


#Predikera för 2025
aktuella_år = (moore[:, 0] < 2020) & (moore[:, 0] > 1971)  
år = moore[aktuella_år, 0]
X  = np.ones((len(år), 2))
X[:, 1] = år
antal_resistorer = moore[aktuella_år, 1]
w = np.log(antal_resistorer)
beta_hat, beta_interval = tools.regress(X, w)

år = np.linspace(1971, 2025, (2025-1971)*10)
X  = np.ones((len(år), 2))
X[:, 1] = år
pred_2025 = np.exp(beta_hat[0] + beta_hat[1]*2025)
print(f'Förväntat antal transistorer 2025: {pred_2025}')
plt.figure()
plt.plot(år, np.exp(X @ beta_hat), 'r')
plt.scatter(moore[:, 0], moore[:, 1])
plt.plot(2025, pred_2025, 'g*', markersize=10)
plt.xlabel('År')
plt.ylabel('Antal transistorer')
plt.legend(['Linjär regression', 'Data', 'Prediktion 2025'])
plt.show()