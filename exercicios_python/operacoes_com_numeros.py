from time import sleep

print("\n")
primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opcao = int(input("Qual a sua opção?: "))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} e {segundo} é {soma}')
        print("=" * 30)
    elif opcao == 2:
        multiplicacao = primeiro * segundo
        print(f'A multiplicação entre {primeiro} e {segundo} é {multiplicacao}')
        print("=" * 30)
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
            print(f'O maior valor é {maior}')
            print("=" * 30)
        elif primeiro < segundo:
            maior = segundo
            print(f'O maior valor é {maior}')
            print("=" * 30)
        else:
            print("Os números são iguais!")
    elif opcao == 4:
        print("Informe os numeros novamente: ")
        primeiro = int(input("Primeiro valor: "))
        segundo = int(input("Segundo valor: "))
        print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        ''')
        opcao = int(input("Qual a sua opção?: "))
        if opcao == 1:
            soma = primeiro + segundo
            print(f'A soma entre {primeiro} e {segundo} é {soma}')
            print("=" * 30)
        elif opcao == 2:
            multiplicacao = primeiro * segundo
            print(f'A multiplicação entre {primeiro} e {segundo} é {multiplicacao}')
            print("=" * 30)
        elif opcao == 3:
            if primeiro > segundo:
                maior = primeiro
                print(f'O maior valor é {maior}')
                print("=" * 30)
            elif primeiro < segundo:
                maior = segundo
                print(f'O maior valor é {maior}')
                print("=" * 30)
            else:
                print("Os números são iguais!")
        elif opcao == 4:
            print("Informe os numeros novamente: ")
            primeiro = int(input("Primeiro valor: "))
            segundo = int(input("Segundo valor: "))
            print('''
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
            ''')
    elif opcao == 5:
        print("Finalizando...")
        sleep(1)
        print("Fim do programa! Volte sempre!")
    else:
        print("opcao invalida..tente novamente!")
        print("=" * 30)


        