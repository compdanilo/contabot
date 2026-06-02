from __future__ import annotations

import re
from datetime import datetime


REGEX_CNPJ = re.compile(r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}")
REGEX_DATA = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
REGEX_VALOR = re.compile(r"R\$\s?\d+(?:\.\d{3})*,\d{2}")


def _somente_digitos(texto: str) -> str:
    return re.sub(r"\D", "", texto)


def validar_cnpj(cnpj: str) -> bool:
    """Valida CNPJ usando o cálculo oficial dos dígitos verificadores."""
    cnpj_limpo = _somente_digitos(cnpj)

    if len(cnpj_limpo) != 14:
        return False

    if cnpj_limpo == cnpj_limpo[0] * 14:
        return False

    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo = [6] + pesos_primeiro

    def calcular_digito(base: str, pesos: list[int]) -> str:
        soma = sum(int(digito) * peso for digito, peso in zip(base, pesos))
        resto = soma % 11
        return "0" if resto < 2 else str(11 - resto)

    primeiro_digito = calcular_digito(cnpj_limpo[:12], pesos_primeiro)
    segundo_digito = calcular_digito(cnpj_limpo[:12] + primeiro_digito, pesos_segundo)
    return cnpj_limpo[-2:] == primeiro_digito + segundo_digito


def extrair_cnpj(texto: str) -> str | None:
    """Retorna o primeiro CNPJ encontrado no texto."""
    encontrado = REGEX_CNPJ.search(texto)
    return encontrado.group(0) if encontrado else None


def validar_data(data_texto: str) -> bool:
    """Valida data no formato dd/mm/aaaa."""
    try:
        datetime.strptime(data_texto, "%d/%m/%Y")
    except ValueError:
        return False
    return True


def extrair_datas(texto: str) -> list[str]:
    """Extrai datas válidas no formato dd/mm/aaaa."""
    datas = REGEX_DATA.findall(texto)
    return [data for data in datas if validar_data(data)]


def extrair_valores(texto: str) -> list[str]:
    """Extrai valores monetários no padrão brasileiro."""
    return REGEX_VALOR.findall(texto)


def obter_status_validacao(
    cnpj_encontrado: str | None, cnpj_valido: bool, datas: list[str], valores: list[str]
) -> tuple[str, str]:
    """Monta status geral de validação e observações úteis para o relatório."""
    observacoes: list[str] = []

    if not cnpj_encontrado:
        observacoes.append("CNPJ não encontrado")
    elif not cnpj_valido:
        observacoes.append("CNPJ inválido")

    if not datas:
        observacoes.append("Nenhuma data válida encontrada")

    if not valores:
        observacoes.append("Nenhum valor monetário encontrado")

    if observacoes:
        return "pendente", "; ".join(observacoes)

    return "ok", "Validação concluída com sucesso"
