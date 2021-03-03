i = 1
while True:
    num = int(input("\nQuer ver a tabuada de qual valor? "))
    print("-" * 40)
    if num < 0:
        break
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
        i += 1
    print("-" * 40)
print("Programa encerrado")