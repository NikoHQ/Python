import pandas as pd 
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1iniHOoi-SXq9yHJRccKD_BOWuGRdzTA2uSD9y12HxfE/export?format=csv")

df.plot.scatter(x='Altura', y='Peso')
reg = LinearRegression()
reg.fit(df[["Altura"]], df["Peso"])
reg.predict([[1.40],[1.90]])

print(f"la línea intersecta en : {reg.intercept_} y tiene una pendiente de { reg.coef_}")
reg.coef_ * df["Altura"] + reg.intercept_
pred = pd.Series(reg.predict(df[["Altura"]]))
df["prediccion"] = pred

ax = df.plot.line(x="Altura", y="prediccion")
df.plot.scatter(x="Altura", y="Peso", ax= ax, color="#2d0c62", figsize=(12,7))
plt.show()