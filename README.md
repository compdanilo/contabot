# ContaBot

RPA em Python para organização e validação de documentos contábeis.

## Sobre

O **ContaBot** é um projeto de automação voltado para rotinas contábeis repetitivas, como organização de arquivos, validação de dados básicos e geração de relatórios simples.

A ideia é construir um MVP aplicando conceitos de **RPA**, **QA**, **validação de dados** e **Python**.

## Funcionalidades planejadas

- [ ] Ler arquivos de uma pasta de entrada
- [ ] Organizar documentos por tipo
- [ ] Validar CNPJ
- [ ] Validar datas e valores
- [ ] Gerar relatório em Excel
- [ ] Criar testes automatizados

## Estrutura

```text
contabot/
├── data/
│   ├── entrada/
│   └── saida/
├── src/
│   ├── main.py
│   ├── organizador.py
│   ├── validador.py
│   └── relatorio.py
├── tests/
│   └── test_validador.py
├── README.md
├── requirements.txt
└── .gitignore
