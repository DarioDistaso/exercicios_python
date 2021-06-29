from datetime import date

anoAtual = date.today().year
dicionario = dict()

dicionario['Nome'] = str(input("Nome: "))
anoNasc = int(input("Ano de nascimento: "))
dicionario['Idade'] = anoAtual - anoNasc
dicionario['Ctps'] = int(input("Carteira de trabalho (0 nao tem): "))

if dicionario['Ctps'] == 0:
    print("-=" * 20)
else:
    dicionario['Contratação'] = int(input("Ano de contratação: "))
    dicionario['Salario'] = float(input("Salário: R$ "))
    dicionario['Aposentadoria'] = (dicionario['Contratação'] + 35) - anoNasc
    print("-=" * 20)

for k,v in dicionario.items():
    print(f'- {k} tem valor {v}')