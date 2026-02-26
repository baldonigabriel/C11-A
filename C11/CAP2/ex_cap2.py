# Exercício 1

nome = input("Digite seu nome completo: ").strip()

print("MAIÚSCULAS:", nome.upper())
print("minúsculas:", nome.lower())

qtd_letras = sum(1 for c in nome if c != " ")
print("Total de letras:", qtd_letras)

partes = nome.split()
if len(partes) >= 2:
    novo_nome = " ".join(partes[:-1] + ["do Inatel"])
else:
    novo_nome = nome + " do Inatel"

print("Trocando o último nome:", novo_nome)

# Exercício 2

inicio = int(input("Início do intervalo: "))
fim = int(input("Fim do intervalo: "))

if inicio > fim:
    inicio, fim = fim, inicio

n = int(input(f"Escolha um número entre {inicio} e {fim}: "))

while n < inicio or n > fim:
    n = int(input(f"Fora do intervalo! Digite entre {inicio} e {fim}: "))

print(f"Tabuada do {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Exercício 3

sexo = input("Digite o sexo (M/F): ").strip().upper()

while sexo != "M" and sexo != "F":
    sexo = input("Inválido! Digite o sexo (M/F): ").strip().upper()

if sexo == "M":
    print("Você é homem.")
else:
    print("Você é mulher.")

# Exercício 4

km = float(input("Distância da viagem (km): ").replace(",", "."))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print(f"Preço da passagem: R$ {preco:.2f}")

# Exercício 5

n = int(input("Digite um número entre 1000 e 9999: "))

while n < 1000 or n > 9999:
    n = int(input("Inválido! Digite um número entre 1000 e 9999: "))

unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)

# Exercício 6

import math

x = float(input("Digite um número decimal: ").replace(",", "."))

if x < 0:
    print("Raiz quadrada: não existe (número negativo).")
else:
    print("Raiz quadrada:", math.sqrt(x))

print("Função teto (ceil):", math.ceil(x))
print("Função chão (floor):", math.floor(x))
print("Parte inteira (trunc):", math.trunc(x))