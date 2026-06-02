from src.validador import extrair_cnpj, extrair_datas, extrair_valores, validar_cnpj


def test_validar_cnpj_valido() -> None:
    assert validar_cnpj("11.222.333/0001-81") is True


def test_validar_cnpj_invalido() -> None:
    assert validar_cnpj("11.222.333/0001-82") is False


def test_extrair_cnpj() -> None:
    texto = "Fornecedor XPTO - CNPJ: 11.222.333/0001-81"
    assert extrair_cnpj(texto) == "11.222.333/0001-81"


def test_extrair_datas() -> None:
    texto = "Competência: 10/05/2026. Pagamento previsto para 31/12/2026."
    assert extrair_datas(texto) == ["10/05/2026", "31/12/2026"]


def test_extrair_valores() -> None:
    texto = "Valor principal: R$ 1.250,90 e valor adicional: R$ 90,00."
    assert extrair_valores(texto) == ["R$ 1.250,90", "R$ 90,00"]
