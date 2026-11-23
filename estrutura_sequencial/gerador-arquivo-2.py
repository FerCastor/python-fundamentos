from pathlib import Path

# Define o diretório atual onde o script está sendo executado
pasta_atual = Path.cwd()

for i in range(1, 19):
    # Formata o número com 3 dígitos (ex: 1 vira '001')
    nome_arquivo = f"ex{i:03d}.py"
    caminho_completo = pasta_atual / nome_arquivo

    # Cria o arquivo vazio (se já existir, não sobrescreve o conteúdo)
    caminho_completo.touch(exist_ok=True)

print("Os arquivos foram criados com sucesso!")
