print("Organizador de Arquivos - Projeto de Portifolio")

import os
import shutil

# Caminho da pasta que será organizada
CAMINHO_PASTA = "arquivos_para_organizar"

# Dicionário: extensão -> nome da pasta
MAPA_PASTAS = {
    ".pdf": "PDFs",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".mp4": "Videos",
    ".txt": "Textos"
}

def organizar_arquivos():
    # Verifica se a pasta existe
    if not os.path.exists(CAMINHO_PASTA):
        print("Pasta não encontrada.")
        return

    # Lista todos os arquivos da pasta
    for arquivo in os.listdir(CAMINHO_PASTA):
        caminho_arquivo = os.path.join(CAMINHO_PASTA, arquivo)

        # Ignora pastas
        if os.path.isdir(caminho_arquivo):
            continue

        # Separa nome e extensão
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        # Verifica se a extensão está mapeada
        if extensao in MAPA_PASTAS:
            pasta_destino = MAPA_PASTAS[extensao]
        else:
            pasta_destino = "Outros"

        caminho_destino = os.path.join(CAMINHO_PASTA, pasta_destino)

        # Cria a pasta se não existir
        os.makedirs(caminho_destino, exist_ok=True)

        # Move o arquivo
        shutil.move(caminho_arquivo, caminho_destino)

        print(f"{arquivo} movido para {pasta_destino}")

if __name__ == "__main__":
    organizar_arquivos()
