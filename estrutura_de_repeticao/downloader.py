from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = "https://exercicios.dunossauro.com/03_estrutura_de_repeticao/"
pasta_destino = Path(__file__).parent

# Baixa o conteúdo HTML da página
resposta = requests.get(url)
resposta.raise_for_status()

soup = BeautifulSoup(resposta.text, "html.parser")

# Percorre todos os títulos h4 (onde ficam os nomes "Exercício 1", "Exercício 2", etc.)
for titulo in soup.find_all("h4"):
    texto_titulo = titulo.get_text(strip=True)

    if texto_titulo.startswith("Exercício "):
        # Extrai o número do exercício para formatar como ex001.py
        numero = int(texto_titulo.split()[1])
        nome_arquivo = f"ex{numero:03d}.py"

        enunciado = []
        # Pega todos os elementos irmãos seguintes até encontrar o próximo exercício ou o editor
        for irmao in titulo.find_next_siblings():
            if irmao.name == "h4":
                break
            # Ignora as caixas de código/editor interativo da página
            if irmao.name in ["p", "ul", "ol", "pre", "blockquote"]:
                enunciado.append(irmao.get_text(" ", strip=True))

        texto_final = "\n\n".join(enunciado)

        # Monta o conteúdo do arquivo .py com o enunciado comentado no topo
        conteudo_py = f'"""\n{texto_titulo}\n\n{texto_final}\n"""\n\n# Escreva sua solução abaixo:\n'

        caminho_arquivo = pasta_destino / nome_arquivo
        caminho_arquivo.write_text(conteudo_py, encoding="utf-8")

print("Todos os exercícios foram baixados e salvos com sucesso!")