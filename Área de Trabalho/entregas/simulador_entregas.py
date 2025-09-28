def calcular_tempo(distancia_km, velocidade_kmh):
    tempo_horas = distancia_km / velocidade_kmh
    return tempo_horas * 60  # minutos

def simular_entrega(nome, origem, destino, distancia_km, velocidade_kmh, valor_entrega):
    tempo = calcular_tempo(distancia_km, velocidade_kmh)
    print(f"\n🛵 Simulação de entrega para {nome}")
    print(f"De: {origem}")
    print(f"Para: {destino}")
    print(f"Distância: {distancia_km} km")
    print(f"Tempo estimado: {tempo:.1f} minutos")
    print(f"Valor recebido: R${valor_entrega:.2f}")
    ganho_por_hora = valor_entrega / (tempo / 60)
    print(f"💰 Rendimento por hora: R${ganho_por_hora:.2f}")

# Exemplo de uso:
simular_entrega(
    nome="João",
    origem="Brasilândia",
    destino="Centro",
    distancia_km=10,
    velocidade_kmh=20,
    valor_entrega=7.50
)