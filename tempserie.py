# importando modulos necesarios
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import statsmodels.api as sm 

data = pd.read_csv('/home/tincho/Desktop/Caos/Tp/TP3/osc15-EST-01.csv', delimiter=";")

Tiempo = data['Tiempo'].tolist()
Velocidad = data['Velocidad'].tolist()
R = data['R'].tolist()
T = data['T'].tolist()

data_ma = data['R'].rolling(5).mean()
data['prod_mov'] = data_ma
plot = data[['R', 'prod_mov']].plot(figsize=(10, 8), fontsize=12)
plt.show()

descomposicion = sm.tsa.seasonal_decompose(data['T'],
                                                  model='additive', freq=30)  
fig = descomposicion.plot()
plt.show()