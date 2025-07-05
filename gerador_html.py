import json
from string import Template
import os

# Carrega os dados do JSON
with open("dados_musicas.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Lê o template
with open("templates/modelo_instrumento.html", "r", encoding="utf-8") as f:
    template = Template(f.read())

# Gera os HTMLs
for musica_id, info in dados.items():
    for instrumento, conteudo in info["instrumentos"].items():
        html = template.substitute(
            instrumento=instrumento.capitalize(),
            musica=info["titulo"],
            audio=conteudo["audio"],
            video=conteudo["video"],
            partitura=conteudo["partitura"]
        )

        # Cria a pasta destino se não existir
        pasta_destino = f"repertorio/{musica_id}"
        os.makedirs(pasta_destino, exist_ok=True)

        # Nome do arquivo
        nome_arquivo = f"{instrumento}_{musica_id}.html"
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)

        # Salva o HTML gerado
        with open(caminho_completo, "w", encoding="utf-8") as saida:
            saida.write(html)

print("🎉 HTMLs gerados com sucesso!")
