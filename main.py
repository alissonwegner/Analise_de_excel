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
