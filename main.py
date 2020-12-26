from numpy.core.fromnumeric import std
import pandas as pd
import math
import statistics
import numpy as np


# pd.set_option('display.max_rowns', 1000)#limitando linha e coluna
#pd.set_option('display.max_', 1000)

banco = pd.read_excel("bb.xls")
banco.head()
#print(banco)

dados = banco[['Café']].describe()
#print(dados)

cont = dados.describe().loc[['count']]#conta valor de linhas
mean = dados.describe().loc[['mean']]#media
std_ = dados.describe().loc[['std']]#Desvio padrão
min = dados.describe().loc[['min']]#minimo
max = dados.describe().loc[['max']]#maximo
q1 = dados.describe().loc[['25%']]#quatil1
q2 = dados.describe().loc[['50%']]#quatil2
q3 = dados.describe().loc[['75%']]#quatil3
mediana = dados[['Café']].median()#mediana
print("mediana   ", mediana)
amplitude = max - min
ncolunas = len(banco.index)  # numero de linhas
k = math.sqrt(ncolunas)
h = amplitude / k
print(banco['Café'].mode())

