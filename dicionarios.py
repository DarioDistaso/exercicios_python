D = {'nome' : 'Dario', 'sobrenome' : 'Distaso', 'idade' : 49, 'data_nasc' : '07/10/1971' }
ordenada = list(D.keys())

print(ordenada)
ordenada.sort()
print(ordenada)

for chave in ordenada:
    print (chave, "=", D[chave])