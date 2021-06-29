soma = 0
contasexo = 0
idoso = ''
idademaior = 0
for i in range(1,5):
    print("-----", i, "° PESSOA-----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma += idade
    if sexo == "f" and idade < 20:
        contasexo += 1
    if i == 1 and sexo in "mM":
        idademaior = idade
        idoso = nome
    elif sexo in "mM" and idade > idademaior:
        idademaior = idade
        idoso = nome

media = soma / 4
print(f'a média de idade do grupo é de {media} anos')
print(f'o homem mais velho tem {idademaior} anos e se chama {idoso}')
print(f'Ao todo são {contasexo} mulheres com menos de 20 anos')


