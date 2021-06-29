print("-" * 30)
print("      LOJA SUPER BARATÃO")
print("-" * 30)
total = 0
mil_reais = 0
barato = 10000000
barbada = 0

while True:
    produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço: R$ "))
    cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    total += preco
    
    if preco < barato:
        barato = preco
        barbada = produto

    if preco > 1000:
        mil_reais += 1
    
    if cont == 'N':
        print("-" * 30, "FIM DO PROGRAMA", "-" * 30)
        break

print(f'''O total da compra foi R$ {total}
Temos {mil_reais} produtos custando mais de R$ 1000.00
O produto mais barato foi {barbada} que custa R$ {barato}''')
    
