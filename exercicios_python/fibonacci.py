# 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55 - etc..

print("-" * 30)
print("Sequência de Fibonacci")
print("-" * 30)

numero = int(input("Quantos numeros quer mostrar?: "))
print("~" * 60)

primeiro = 0
segundo = 1

soma = 0
print(primeiro, " → ", segundo, end = "")

i = 2
while i < numero:
    soma = primeiro + segundo
    print(" → ", soma, end = "")
    primeiro = segundo
    segundo = soma
    i += 1
print(" → FIM")
print("~" * 60) 