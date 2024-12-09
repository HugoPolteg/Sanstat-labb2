import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting
import math
import random


def train_test_split(X, y, ratio):
    
    indices = np.array(range(len(X)))

    train_size = round(ratio*len(X))

    random.shuffle(indices)
    train_indices = indices[0:train_size]
    test_indices = indices[train_size:len(X)]
    X_train = X[train_indices, :]
    X_test = X[test_indices, :]
    y_train = y[train_indices]
    y_test = y[test_indices]
    return X_train, X_test, y_train, y_test

def normal_equation(X, y):
    beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y
    return beta_hat

def predict(X_test, beta_hat):
    return X_test @ beta_hat

#Multipel linjär regression
# Ladda data
birth = np.loadtxt('birth.dat')
#Enkel linjär regression på födelsevikt och moderns längd
nonans = ~np.isnan(birth[:, 2]) & ~np.isnan(birth[:, 15])
X = birth[nonans, 15]
X = np.c_[np.ones(len(X)), X]
y = birth[nonans, 2]
beta_hat, beta_interval = tools.regress(X, y)
print(f'Betaväde: {beta_hat[1]}')
plt.figure()
plt.scatter(X[:, 1], y)
plt.plot(X[:, 1], X @ beta_hat, 'r')
plt.xlabel('Moders längd')
plt.ylabel('Födelsevikt')
plt.legend(['Data', 'Linjär regression'])
plt.title('Födelsevikt och moderns längd')
plt.show()
#Multipel linjär regression på födelsevikt mot moderns längd, moderns vikt, moderns rökvanor och nivå av träning
# Födelsevikt är på index 2, moderns vikt på index 14, moderns rökvanor på index 19 och nivå av träning på index 24
nonans = ~np.isnan(birth[:, 2]) & ~np.isnan(birth[:, 14]) & ~np.isnan(birth[:, 19]) & ~np.isnan(birth[:, 24])
X = birth[:, [14, 19, 24]]
X = X[nonans]
X = np.c_[np.ones(len(X)), X]
#Sätt kategoriska värden till 0 eller 1
rökare = (X[:, 2] == 3)
icke_rökare = (X[:, 2] < 3)
tränar = (X[:, 3] == 3)
tränar_inte = (X[:, 3] < 3)
X[rökare, 2] = 1
X[icke_rökare, 2] = 0
X[tränar, 3] = 1
X[tränar_inte, 3] = 0
y = birth[nonans, 2]
beta_hat, beta_interval = tools.regress(X, y)
print(f'Övre gräns för konfidensintervallet för moderns vikt: {beta_interval[1][1]}, nedre gräns: {beta_interval[1][0]}')
print(f'Övre gräns för konfidensintervallet för moderns rökvanor: {beta_interval[2][1]}, nedre gräns: {beta_interval[2][0]}')
print(f'Övre gräns för konfidensintervallet för moderns träningsvanor: {beta_interval[3][1]}, nedre gräns: {beta_interval[3][0]}')
if beta_interval[1][0] < 0 and beta_interval[1][1] > 0:
    print('Konfidensintervallet för moderns vikt inkluderar noll')
elif beta_interval[1][0] > 0:
    print('Konfidensintervallet för moderns vikt är positivt')
else:
    print('Konfidensintervallet för moderns vikt är negativt')
if beta_interval[2][0] < 0 and beta_interval[2][1] > 0:
    print('Konfidensintervallet för moderns rökvanor inkluderar noll')
elif beta_interval[2][0] > 0:
    print('Konfidensintervallet för moderns rökvanor är positivt')
else:
    print('Konfidensintervallet för moderns rökvanor är negativt')
if beta_interval[3][0] < 0 and beta_interval[3][1] > 0:
    print('Konfidensintervallet för moderns träningsvanor inkluderar noll')
elif beta_interval[3][0] > 0:
    print('Konfidensintervallet för moderns träningsvanor är positivt')
else:
    print('Konfidensintervallet för moderns träningsvanor är negativt')
#Kontrollräkning
split = 0.7
X_train, X_test, y_train, y_test = train_test_split(X, y, split)
beta = normal_equation(X_train, y_train)
y_pred = predict(X_test, beta)
print(f'Fel mellan regress(metod) och kontrollräkning: {np.linalg.norm(beta_hat - beta)}')

res = y - X @ beta_hat
_ = stats.probplot(res, plot=plt)
plt.show()