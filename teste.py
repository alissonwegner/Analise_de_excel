import pandas as pd
import math
df = pd.read_excel("bb.xls")
#df = data['fixed acidity']
#df.sort_values(by=Café, ascending=True)
at = df.max() - df.min()
  # Lembrando que k = raiz quadrada do total de registros/amostras
k = math.sqrt(len(df))
    # O valor de amplitude de classe pode ser arredondado para um número inteiro, geralmente para facilitar a interpretação da tabela.
h = at/k 
h = math.ceil(h)
frequencias = []

# Menor valor da série
menor = round(df.min(),1)

# Menor valor somado a amplitude
menor_amp = round(menor+h,1)

valor = menor
while valor < df.max():
    frequencias.append('{} - {}'.format(round(valor,1),round(valor+h,1)))
    valor += h
    freq_abs = pd.qcut(df,len(frequencias),labels=frequencias) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print(pd.value_counts(freq_abs))