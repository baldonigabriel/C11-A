# Exercício 1

times = ["Real Madrid", "Barcelona", "Manchester City", "Bayern", "PSG"]

print("3 primeiros:", times[:3])
print("Últimos 2:", times[-2:])
print("Ordem alfabética:", sorted(times))

pos_barcelona = times.index("Barcelona") + 1
print("Barcelona está na posição:", pos_barcelona)

# Exercício 2

loja1 = {"iPhone 13", "Galaxy S22", "Moto G84", "Xiaomi 12"}
loja2 = {"iPhone 13", "Galaxy S23", "Moto G84", "Pixel 7"}

print("Modelos loja 1:", loja1)
print("Modelos loja 2:", loja2)

total = loja1 | loja2
print("Total de modelos (visitando as duas):", total)

ambas = loja1 & loja2
print("Modelos disponíveis nas duas lojas:", ambas)

# Exercício 3

aluno = {}

aluno["nome"] = input("Nome do aluno: ").strip()
aluno["media"] = float(input("Média do aluno: ").replace(",", "."))

aluno["situacao"] = "AP" if aluno["media"] >= 50 else "RP"

print("\nDicionário do aluno:")
print(aluno)

# Exercício 4

pessoas = []

for i in range(1, 4):
    nome = input(f"Nome da {i}ª pessoa: ").strip()
    peso = float(input(f"Peso da {i}ª pessoa (kg): ").replace(",", "."))
    pessoas.append({"nome": nome, "peso": peso})

mais_pesada = max(pessoas, key=lambda p: p["peso"])
mais_leve = min(pessoas, key=lambda p: p["peso"])

print("\nMais pesada:", mais_pesada["nome"], "-", mais_pesada["peso"], "kg")
print("Mais leve:", mais_leve["nome"], "-", mais_leve["peso"], "kg")

# Exercício 5

pessoas = []

n = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(1, n + 1):
    nome = input(f"\nNome da {i}ª pessoa: ").strip()
    idade = int(input("Idade: "))

    sexo = input("Sexo (M/F): ").strip().upper()
    while sexo != "M" and sexo != "F":
        sexo = input("Inválido! Sexo (M/F): ").strip().upper()

    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

media_idade = sum(p["idade"] for p in pessoas) / len(pessoas)
mulheres_menos_20 = sum(1 for p in pessoas if p["sexo"] == "F" and p["idade"] < 20)

print("\n--- RESULTADOS ---")
print(f"Média de idade do grupo: {media_idade:.2f}")

print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")
