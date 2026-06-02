from __future__ import annotations

from pathlib import Path

from src.organizador import identificar_tipo_documento, listar_arquivos_entrada, organizar_arquivo
from src.relatorio import gerar_relatorio_excel
from src.validador import (
    extrair_cnpj,
    extrair_datas,
    extrair_valores,
    obter_status_validacao,
    validar_cnpj,
)


def carregar_texto_arquivo(caminho_arquivo: Path) -> str:
    try:
        return caminho_arquivo.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return caminho_arquivo.read_text(encoding="latin-1", errors="ignore")


def processar_documentos() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    pasta_entrada = base_dir / "data" / "entrada"
    pasta_saida = base_dir / "data" / "saida"
    caminho_relatorio = pasta_saida / "relatorio_validacao.xlsx"

    arquivos = listar_arquivos_entrada(pasta_entrada)
    if not arquivos:
        print("Nenhum arquivo encontrado em data/entrada.")
        return

    registros: list[dict] = []
    processados = 0

    for arquivo in arquivos:
        texto = carregar_texto_arquivo(arquivo)
        tipo_documento = identificar_tipo_documento(arquivo.name)

        cnpj_encontrado = extrair_cnpj(texto) or extrair_cnpj(arquivo.name)
        cnpj_valido = validar_cnpj(cnpj_encontrado) if cnpj_encontrado else False

        datas_encontradas = extrair_datas(texto)
        valores_encontrados = extrair_valores(texto)

        status, observacoes = obter_status_validacao(
            cnpj_encontrado=cnpj_encontrado,
            cnpj_valido=cnpj_valido,
            datas=datas_encontradas,
            valores=valores_encontrados,
        )

        organizar_arquivo(
            caminho_arquivo=arquivo,
            pasta_saida_base=pasta_saida,
            tipo_documento=tipo_documento,
            mover=False,
        )

        registros.append(
            {
                "nome_arquivo": arquivo.name,
                "tipo_documento": tipo_documento,
                "cnpj_encontrado": cnpj_encontrado or "",
                "cnpj_valido": cnpj_valido,
                "datas_encontradas": "; ".join(datas_encontradas),
                "valores_encontrados": "; ".join(valores_encontrados),
                "status": status,
                "observacoes": observacoes,
            }
        )
        processados += 1
        print(f"Arquivo processado: {arquivo.name} -> tipo {tipo_documento}")

    gerar_relatorio_excel(registros, caminho_relatorio)
    print("\nResumo da execução:")
    print(f"- Total de arquivos processados: {processados}")
    print(f"- Relatório gerado em: {caminho_relatorio}")
    print(f"- Arquivos organizados em: {pasta_saida}")


if __name__ == "__main__":
    processar_documentos()
