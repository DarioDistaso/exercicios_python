print("-=" * 30)
tupla = ('dario', 'bea', 'gabi', 'nice', 'mercia', 'andre', 'marisa', 'massi', 'sogand', 'salvatore', 'gianni', 'laerte', 'pinuccio', 'francesca', 'gennaro', 'antonietta', 'maria', 'nunzio', 'claudia', 'barbara')
print(f'lista de nomes aleatória: {tupla}')
print("-=" * 30)

print('Os 5 primeiros são:', end = " ")
for i in range(0,5):
    print(tupla[i], end = ' ')
print("\n", "-=" * 30)
print('\nOs ultimos 4 são:', end = " ")
for j in range(16, len(tupla)):
    print(tupla[j], end = ' ')
print("\n", "-=" * 30)

print(f'\nNomes em ordem alfabética: {sorted(tupla)}')
print("-=" * 30)
print(f'O Massi está na {tupla.index("massi") + 1} posição')

