# Projeto de Exercícios Python

Este projeto reúne exemplos e explicações em Python para fundamentos de programação, lógica condicional, loops e manipulação de entrada/saída.

## Estrutura do projeto

- `test-assistent-code/`
  - `debug.py` - script interativo que calcula o total de uma compra com imposto e desconto.
  - `num_primos.py` - função para verificar se um número é primo, com exemplos de execução.
  - `refatoracao.py` - função que calcula estatísticas básicas (soma, média, maior e menor valor) de uma lista de números.
  - `explicacao-debug.md` - explicação sobre erros identificados e correções aplicadas no código `debug.py`.
  - `explicacao_num_primo.md` - explicação detalhada do algoritmo usado para verificar números primos.
  - `explicacao_refatoracao.md` - explicação detalhada do código original e sugestões de refatoração.

## Visão geral dos scripts

### `debug.py`

Este script pede ao usuário dados sobre três itens de compra:
- nome do cliente
- quantidade e preço de cada item
- percentual de desconto aplicável

Em seguida, calcula e exibe:
- total de cada item
- subtotal
- imposto fixo de 10%
- desconto percentual
- total final formatado

### `num_primos.py`

Contém a função `eh_primo(numero)` que determina se um número é primo usando verificações sucessivas:
- rejeita números menores que 2
- aceita 2 diretamente
- rejeita números pares maiores que 2
- testa divisores ímpares até a raiz quadrada do número

O arquivo também inclui um bloco de testes que executa a função em vários valores e imprime o resultado.

### `refatoracao.py`

Apresenta a função `calcular_estatisticas_basicas(numeros)` que calcula:
- soma total
- média
- maior valor
- menor valor

A função valida que a lista não esteja vazia e usa funções built-in do Python para simplificar os cálculos.

## Como executar

Certifique-se de ter Python 3 instalado.

Execute os scripts diretamente no terminal:

```bash
python test-assistent-code/debug.py
python test-assistent-code/num_primos.py
python test-assistent-code/refatoracao.py
```

## Observações

- Os scripts são independentes e não requerem dependências externas.
- Os arquivos Markdown (`explicacao-*.md`) oferecem material de suporte para entender a lógica e possíveis melhorias.
- O projeto é adequado para estudo de lógica básica em Python, tratamento de entrada/saída e análise de algoritmos simples.

## Sugestões de evolução

- Adicionar testes automatizados usando `unittest` ou `pytest`.
- Transformar `debug.py` em funções reutilizáveis para separar cálculo e interface.
- Melhorar a validação de entradas do usuário em `debug.py`.
- Incluir type hints em todos os scripts para maior clareza.
