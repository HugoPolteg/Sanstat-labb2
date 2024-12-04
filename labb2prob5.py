import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tools
import plotting

#Ladda data
birth = np.loadtxt('birth.dat')

#Extrahera kolumner för att kolla om de är normalfördelade
birth_weight = birth[:, 2]
birth_weight = birth_weight[~np.isnan(birth_weight)]

mother_age = birth[:, 3]
mother_age = mother_age[~np.isnan(mother_age)]

mother_length = birth[:, 15]
mother_length = mother_length[~np.isnan(mother_length)]

mother_weight = birth[:, 14]
mother_weight = mother_weight[~np.isnan(mother_weight)]

#använd probplot för att kolla om de är normalfördelade
plt.figure()
_ = stats.probplot(birth_weight, plot=plt)
plt.title('Födelsevikt')
plt.show()
_ = stats.probplot(mother_age, plot=plt)
plt.title('Moders ålder')
plt.show()
plt.figure()
_ = stats.probplot(mother_length, plot=plt)
plt.title('Moders längd')
plt.show()
plt.figure()
_ = stats.probplot(mother_weight, plot=plt)
plt.title('Moders vikt')
plt.show()

#H0: X är normalfördelad
#H1: X är inte normalfördelad (signifikansnivå 5%)

res = stats.jarque_bera(birth_weight)
if(res.pvalue < 0.05):
    print('Födelsevikt är inte normalfördelad')
else:
    print('Födelsevikt är normalfördelad')
res = stats.jarque_bera(mother_age)
print(res.pvalue)
if(res.pvalue < 0.05):
    print('Moders ålder är inte normalfördelad')
else:
    print('Moders ålder är normalfördelad')
res = stats.jarque_bera(mother_length)
if(res.pvalue < 0.05):
    print('Moders längd är inte normalfördelad')
else:
    print('Moders längd är normalfördelad')
res = stats.jarque_bera(mother_weight)
if(res.pvalue < 0.05):
    print('Moders vikt är inte normalfördelad')
else:
    print('Moders vikt är normalfördelad')