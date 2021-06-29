from random import randint
from time import sleep
print("-" * 20)
print('JOGA NA MEGA SENA')
print("-" * 20)
quant = int(input("Quantos jogos quer que eu sorteie? "))
print('-=' * 5, end = " ") 
print(f'SORTEANDO {quant} JOGOS', end = " ") 
print("-=" * 5)
lista = []
for i in range(quant):
    for x in range(6):
        num = randint(1,60)
        while num in lista:
            num = randint(1,60)
        lista.append(num)
    lista.sort()
    print(f'Jogo {i+1}:', lista)
    lista.clear()
    sleep(1)
print("-=" * 5, end = " ") 
print("<BOA SORTE!>", end = " ")
print("-=" * 5)