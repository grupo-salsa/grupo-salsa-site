import json

# Carrega os dados de danças a partir do arquivo JSON
with open("dancas.json", encoding="utf-8") as f:
    dancas = json.load(f)

regiao = input("Digite um país onde você viveu ou tem afinidade: ").capitalize()

print("\n🎵 Ritmos da sua região:")
for nome, dados in dancas.items():
    if dados["país"] == regiao:
        print(f"- {nome.title()} (Compasso: {dados['compasso']}, Tipo: {dados['tipo']})")

compasso_pref = input("\nQual compasso te agrada mais? (ex: 2/4, 3/4, 4/4): ")

print("\n🎶 Outras danças com esse compasso:")
for nome, dados in dancas.items():
    if dados["compasso"] == compasso_pref:
        print(f"- {nome.title()} ({dados['país']})")
