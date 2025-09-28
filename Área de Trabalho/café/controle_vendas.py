def calcular_venda(preco_unitario, quantidade):
    return preco_unitario * quantidade

def exibir_relatorio(venda_150ml, venda_80ml):
    total = venda_150ml + venda_80ml
    print("\n=== RELATÓRIO DO DIA ===")
    print(f"Total 150ml: R${venda_150ml:.2f}")
    print(f"Total 80ml : R${venda_80ml:.2f}")
    print(f"TOTAL DO DIA: R${total:.2f}")

# Configurações
preco_150ml = 2.00
preco_80ml = 1.00

# Entrada do usuário
qtd_150ml = int(input("Quantos copos de 150ml você vendeu hoje? "))
qtd_80ml = int(input("Quantos copos de 80ml você vendeu hoje? "))

# Cálculo
venda_150ml = calcular_venda(preco_150ml, qtd_150ml)
venda_80ml = calcular_venda(preco_80ml, qtd_80ml)

# Resultado
exibir_relatorio(venda_150ml, venda_80ml)