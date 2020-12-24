from numpy.core.fromnumeric import std
import pandas as pd
import math

# pd.set_option('display.max_rowns', 1000)#limitando linha e coluna
#pd.set_option('display.max_', 1000)

banco = pd.read_excel("bb.xls")
banco.head()
print(banco)

dados = banco[['Café']].describe()
print(dados)
min = banco[['Café']].min()
min = float(min)
print("valor min do cafe: ", min)
max = banco[['Café']].max()
max = float(max)
print("valor min do cafe: ", max)
amplitude = max - min
# ncolunas=banco.shape
ncolunas = len(banco.index)  # numero de linhas

k = math.sqrt(ncolunas)
h = amplitude / k
teste = dados.describe().loc[['count','max']]
print(teste)