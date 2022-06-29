#Nicolás Robles Alarcón
#Carrera de Ing.Civil Informática secciónI
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#0name,1wins,2kills,3kdRatio,4killstreak,5level,6losses,7prestige,8hits,9timePlayed,10headshots,11averageTime,12gamesPlayed,13assists,14misses,15xp,16scorePerMinute,17shots,18deaths

data = pd.read_csv('cod.csv',delimiter=',')

#data = data.head(1000)

#print(data.columns)
#print(data['kdRatio'])
#print(data)
x = data['timePlayed']
y = data['kills']

reg= LinearRegression()
reg.fit(data[["timePlayed"]],data["kills"])
#reg.predict([[1000]])

print(f"la línea intersecta en : {reg.intercept_} y tiene una pendiente de { reg.coef_}")
reg.coef_ * data["timePlayed"] + reg.intercept_
pred = pd.Series(reg.predict(data[["timePlayed"]]))
data["prediccion"] = pred

ax = data.plot.line(x="timePlayed", y="prediccion")
data.plot.scatter(x="timePlayed", y="kills", ax= ax, color="black", figsize=(12,7))
plt.scatter(x, y, color = 'black')
ax.set(xlabel='Tiempo Jugado(horas)', ylabel='Numero de bajas',
       title='Relacion entre el tiempo de juego de una persona con la cantidad de bajas en Warzone ')

plt.show()