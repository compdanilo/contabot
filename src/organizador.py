from __future__ import annotations

import shutil
from pathlib import Path

TIPOS_DOCUMENTO = ("nota_fiscal", "guia_imposto", "extrato", "recibo", "outros")


def listar_arquivos_entrada(pasta_entrada: Path) -> list[Path]:
    """Lista arquivos da pasta de entrada (sem recursão)."""
    if not pasta_entrada.exists():
        return []
    return [
        caminho
        for caminho in pasta_entrada.iterdir()
        if caminho.is_file() and not caminho.name.startswith(".") and caminho.suffix.lower() == ".txt"
    ]


def identificar_tipo_documento(nome_arquivo: str) -> str:
    """Identifica o tipo com base em palavras-chave no nome do arquivo."""
    nome = nome_arquivo.lower()

    if "nota" in nome or "nf" in nome:
        return "nota_fiscal"
    if "guia" in nome or "imposto" in nome:
        return "guia_imposto"
    if "extrato" in nome or "banco" in nome:
        return "extrato"
    if "recibo" in nome:
        return "recibo"
    return "outros"


def criar_pasta_saida(pasta_saida_base: Path, tipo_documento: str) -> Path:
    """Cria a pasta de saída para o tipo informado."""
    pasta_tipo = pasta_saida_base / tipo_documento
    pasta_tipo.mkdir(parents=True, exist_ok=True)
    return pasta_tipo


def organizar_arquivo(
    caminho_arquivo: Path, pasta_saida_base: Path, tipo_documento: str, mover: bool = False
) -> Path:
    """Copia (ou move) arquivo para a pasta de saída correspondente."""
    destino_pasta = criar_pasta_saida(pasta_saida_base, tipo_documento)
    destino_arquivo = destino_pasta / caminho_arquivo.name

    if mover:
        shutil.move(str(caminho_arquivo), str(destino_arquivo))
    else:
        shutil.copy2(caminho_arquivo, destino_arquivo)

    return destino_arquivo
