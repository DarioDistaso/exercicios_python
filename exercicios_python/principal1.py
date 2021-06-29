from modulos import metade, dobro, aumenta, diminui

print("\033[0;32m")
preco = float(input("\nDigite o preço: "))
pctg = int(input("Digite a taxa porcenual: "))
print("\033[m")
met = metade(preco)
dob = dobro(preco)
aum = aumenta(preco, pctg)
dim = diminui(preco, pctg)


print(f'A metade de R${preco} é {met}')
print(f'O dobro de R${preco} é {dob}')
print(f'Aumentando de {pctg}%, temos R${aum}')
print(f'Diminuindo de {pctg}%, temos R${dim}')