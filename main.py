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
min = banco[['Café']].min()
min = float(min)
max = banco[['Café']].max()
max = float(max)
amplitude = max - min
ncolunas = len(banco.index)  # numero de linhas
k = ncolunas

k=1+3.33*math.log10(340)
k = ("%.0f" % round(k +0.9))
k = int(k)


h = amplitude / k
k = ("%.0f" % round(k +0.9))
h = ("%.2f" % (h+0.04))

#print(banco['Café'].mode())
#classes
aux=1
k = float(k)
h = float(h)
print("h", h)
temp = min

while aux<k:
   print(min)
   clas_tab[aux] = n_classes(min, h)
   min = min + h
   aux=aux+1 
aux=1

while aux<k:
   if(dados.loc[dados.loc['Café']==n_classes.min or dados.loc['Café']< n_classes.max]):
       cont+1
    clas_tab[aux] = n_classes.fre_abs(cont)