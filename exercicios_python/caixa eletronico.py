print("=" * 30)
print('{:^30}'.format('BANCO CEV'))
print("=" * 30)

saque = 0 
sobra = 0
total = 0
cinquenta = 0
vinte = 0
dez = 0
um = 0

while True:
    saque = int(input("Que valor você quer sacar? R$ "))

    if saque >= 50:
        cinquenta = saque // 50
        sobra = saque - (cinquenta * 50)
        total += (cinquenta * 50)
        print(f'Total de {cinquenta} cédulas de R$ 50')

    if sobra >= 20 and sobra < 50: 
        vinte = sobra // 20
        sobra = sobra - (vinte * 20) 
        total += (vinte * 20)
        print(f'Total de {vinte} cédulas de R$ 20')

    if sobra >= 10 and sobra < 20:
        dez = sobra // 10
        sobra = sobra - (dez * 10)
        total += (dez * 10)
        print(f'Total de {dez} cédulas de R$ 10')

    if sobra >= 0 and sobra < 10:
        um = sobra // 1
        sobra = sobra - (um * 1)
        total += (um * 1)
        print(f'Total de {um} cédulas de R$ 1')
    break

print("Volte sempre ao BANCO CEV! Tenha um bom dia!")

