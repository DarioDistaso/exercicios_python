exp = str(input("Digite uma expressão matematica: "))
if exp.count("(") == exp.count(")"):
    print("\033[1;32mA sua expressão é valida!\033[m")
else:
    print("\033[1;31mA sua expressao nao é valida!\033[m")


