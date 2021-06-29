def leiaInt(texto):
    while True:
        num = str(input(texto))
        if not num.isnumeric():
            print("\033[1;31mERRO! Digite um numero inteiro valido!\033[m")
        else:
            return num

n = leiaInt("Digite um numero:")
print(f'Você acabou de digitar o numero {n}')