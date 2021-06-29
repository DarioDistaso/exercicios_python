dicionario = dict()
gols = list()
geral = list()
somaGols = 0

while True:
    dicionario['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas o {dicionario['nome']} jogou? "))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na {i+1}° partida? ')))
        somaGols += gols[i]
    dicionario['gols'] = gols[:]
    dicionario['total'] = somaGols
    geral.append(dicionario.copy())
    perg = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    somaGols = 0
    gols.clear()
    
    if perg in 'N':
        break

print("-=" * 20)
print(geral)

print("cod nome        gols          total")
print("-" * 40)

for z in geral:
    for v in z.values():
        print(f'{v}           ', end = ' ')
    print()

print("-" * 40) 

while True:
    dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if dados == 999:
        break
    while dados >= len(geral):
        print(f'ERRO! Não existe jogador com código {dados}')
        dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    print(f'--- LEVANTAMENTO DO JOGADOR {geral[dados]["nome"]} ---')

    for x in range(len(geral[dados]['gols'])):
        print(f'No jogo {x} fez {geral[dados]["gols"][x]} gols.')
print("<<<VOLTE SEMPRE>>>")



    