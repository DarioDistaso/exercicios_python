dicionario = dict()
lista = list()
soma_idade = mulheres = 0

while True:
    dicionario['nome'] = str(input("Nome: "))
    sexo = str(input("Sexo: [M/F] ")).strip()[0]

    while sexo not in 'MmFf':
        print("ERRO! Por favor, digite apenas M ou F")
        sexo = str(input("Sexo: [M/F] ")).strip()[0]
    else:
        dicionario['sexo'] = sexo
        if sexo in 'Ff':
            mulheres += 1

    dicionario['idade'] = int(input("Idade: "))
    soma_idade += dicionario['idade']
    lista.append(dicionario.copy())
    media = soma_idade / len(lista)
    perg = str(input("Quer continuar? [S/N] ")).strip()[0]

    while perg not in 'SsNn':
        print("ERRO! Responda apenas S ou N.")
        perg = str(input("Quer continuar? [S/N] ")).strip()[0]
       
    if perg in 'Nn':
        break

print("-=" * 30)
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')

print(f'C) As mulheres cadastradas foram {mulheres}:', end = ' ')
for x in lista:
    if x['sexo'] in "Ff":
         print(f'{x["nome"]}', end = ' ')

print('\nD) Lista de pessoas que estão acima da média:')

for x in lista:
    if x['idade'] > media: # o x é cada dicionario na lista. Se colocar dicionario['idade'] retorna o último dicionario 
        for k,v in x.items():
            print(f'    {k} = {v};', end = '')
        print()

print("<<ENCERRADO>>")
