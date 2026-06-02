from __future__ import annotations

from pathlib import Path

import pandas as pd


COLUNAS_RELATORIO = [
    "nome_arquivo",
    "tipo_documento",
    "cnpj_encontrado",
    "cnpj_valido",
    "datas_encontradas",
    "valores_encontrados",
    "status",
    "observacoes",
]


def gerar_relatorio_excel(registros: list[dict], caminho_saida: Path) -> Path:
    """Gera relatório Excel de validação dos documentos."""
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.DataFrame(registros, columns=COLUNAS_RELATORIO)
    dataframe.to_excel(caminho_saida, index=False)
    return caminho_saida
