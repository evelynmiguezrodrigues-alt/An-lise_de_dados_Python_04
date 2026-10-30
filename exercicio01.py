print("Escola Senac\n")
nome = input('Digite o nome do aluno: ').title()

prova1 = float(input("Prova 01: ").replace(",", "."))
prova2 = float(input("Prova 02: ").replace(",", "."))
prova3 = float(input("Prova 03: ").replace(",", "."))

media = (prova1 + prova2 + prova3) / 3

if media >= 7:
    situacao = 'Aprovado'
elif media >= 5:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

print(f'Nome do aluno: {nome.upper()}')
print(f"Prova 1: {prova1:.1f}".replace(".",","))
print(f"Prova 2: {prova2:.1f}".replace(".",","))
print(f"Prova 3: {prova3:.1f}".replace(".",","))
print(f"Média final: {media:.1f}".replace(".",","))

print('Situação: ' + situacao.upper().replace('Ã', 'A'))




