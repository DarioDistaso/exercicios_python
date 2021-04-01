
maior_idade = homens = mulheres = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA: ")
    print("-" * 30)

    idade = int(input("Idade: "))

    if idade > 18:
        maior_idade += 1

    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    
    if sexo == "M":
        homens += 1
    elif sexo == "F":
        if idade < 20:
            mulheres += 1
    else:
        print("digite um valor valido")

    print("-" * 30)

    continua = str(input("Quer continuar? [S/N] "))

    if continua == "n":
        print("\n")
        break
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')