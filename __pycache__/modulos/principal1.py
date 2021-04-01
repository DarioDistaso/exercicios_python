from modulos import metade, dobro, aumenta, diminui, moeda


preco = float(input("Digite o preço: R$ "))
pctg = int(input("Digite a taxa porcenual: "))
met = metade(preco)
dob = dobro(preco)
aum = aumenta(preco, pctg)
dim = diminui(preco, pctg)
m = moeda(preco)


print(f'A metade de {m} é R${met}')
print(f'O dobro de {m} é R${dob}')
print(f'Aumentando de {pctg}%, temos R${aum}')
print(f'Diminuindo de {pctg}%, temos R${dim}')
