# ContaBot

RPA em Python para organização e validação de documentos contábeis.

## Sobre

O **ContaBot** é um projeto de automação voltado para rotinas contábeis repetitivas, como organização de arquivos, validação de dados básicos e geração de relatórios simples.

A ideia é construir um MVP aplicando conceitos de **RPA**, **QA**, **validação de dados** e **Python**.

## Funcionalidades planejadas

- [x] Ler arquivos de uma pasta de entrada
- [x] Organizar documentos por tipo
- [x] Validar CNPJ
- [x] Validar datas e valores
- [x] Gerar relatório em Excel
- [x] Criar testes automatizados

## Estrutura do projeto

- `src/` : código-fonte (processamento, validação e organização)
- `data/entrada/` : coloque os arquivos de texto a serem processados
- `data/saida/` : saída organizada e relatório Excel
- `tests/` : testes automatizados (pytest)
- `README.md`
- `requirements.txt`
- `.gitignore`

## Como usar

1. Ative o ambiente virtual (se houver):

```bash
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Execute o processamento de documentos:

```bash
python -m src.main
```

ou

```bash
python src/main.py
```

## Executando com interface web (Flask)

1. Instale dependências atualizadas (incluindo `flask`):

```bash
pip install -r requirements.txt
```

2. Execute a aplicação web:

```bash
python -m src.web
```
```

Acesse `http://localhost:5000` no navegador para enviar arquivos e gerar o relatório.

## Execução de testes

Para executar os testes:

```bash
pytest -q
```

## Observações

- O leitor de arquivos tenta primeiro `utf-8` e, em caso de erro, usa `latin-1` com `errors="ignore"`.
- Se quiser mover os arquivos em vez de copiá-los, ajuste o parâmetro `mover` na chamada de `organizar_arquivo` em `src/main.py`.
