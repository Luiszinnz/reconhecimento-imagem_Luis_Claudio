# Explicação Detalhada do Código - Verificador de Números Primos

## Visão Geral
Este código implementa uma função que verifica se um número é primo. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

---

## Definição da Função

### Linha 1: Definição da Função
```python
def eh_primo(numero):
```
- Define uma função chamada `eh_primo`
- Recebe um parâmetro chamado `numero` (o número a ser verificado)

### Linhas 2-8: Docstring (Documentação)
```python
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
```
- Texto de documentação que explica o propósito da função
- **Args**: descreve os parâmetros de entrada
- **Returns**: descreve o tipo e valor de retorno

---

## Lógica Principal

### Linha 10: Primeiro Verificação
```python
    if numero < 2:
        return False
```
- **Condição**: verifica se o número é menor que 2
- **Razão**: números menores que 2 (incluindo negativos, 0 e 1) não são primos
- **Retorno**: imediatamente retorna `False` e encerra a função

### Linha 13-14: Caso Especial do 2
```python
    if numero == 2:
        return True
```
- **Condição**: verifica se o número é exatamente 2
- **Razão**: 2 é o único número primo par
- **Retorno**: imediatamente retorna `True` e encerra a função

### Linha 17-18: Verificação de Números Pares
```python
    if numero % 2 == 0:
        return False
```
- **Operador `%`**: calcula o resto da divisão (módulo)
- **Condição**: verifica se o resto da divisão por 2 é zero (número é par)
- **Razão**: todos os números pares maiores que 2 não são primos
- **Retorno**: imediatamente retorna `False` e encerra a função

### Linha 21: Loop de Verificação
```python
    for i in range(3, int(numero**0.5) + 1, 2):
```
- **`range(3, int(numero**0.5) + 1, 2)`**: cria uma sequência de números
  - **Início**: começa em 3 (primeiro ímpar após o 2)
  - **Fim**: vai até a raiz quadrada do número
  - **Passo**: incrementa de 2 em 2 (verifica apenas números ímpares)
- **`numero**0.5`**: calcula a raiz quadrada do número
- **`int(...)`**: converte para número inteiro
- **`+ 1`**: garante que inclua a raiz quadrada inteira
- **Razão**: só precisa testar divisores até a raiz quadrada (otimização)

### Linha 22: Verificação de Divisibilidade
```python
        if numero % i == 0:
            return False
```
- **Condição**: verifica se `numero` é divisível por `i` (resto é zero)
- **Se verdadeiro**: encontrou um divisor, então o número NÃO é primo
- **Retorno**: imediatamente retorna `False` e encerra a função

### Linha 24: Retorno Final
```python
    return True
```
- Se nenhum divisor foi encontrado no loop, o número é primo
- Retorna `True`

---

## Seção de Testes

### Linha 27-28: Comentário e Bloco de Execução
```python
# Exemplos de uso
if __name__ == "__main__":
```
- **`if __name__ == "__main__":`**: verifica se o script está sendo executado diretamente
- Garante que este código só rodará quando o arquivo for executado, não quando importado

### Linha 30: Criação de Lista de Testes
```python
    numeros_teste = [1, 2, 3, 4, 5, 10, 11, 17, 20, 23, 97]
```
- Define uma lista com números para testar
- Inclui: números pequenos, pares, ímpares e números primos conhecidos

### Linha 32: Cabeçalho da Saída
```python
    print("Verificando números primos:\n")
```
- Imprime um título no console
- **`\n`**: quebra de linha para melhor formatação

### Linha 33: Loop de Iteração
```python
    for num in numeros_teste:
```
- Itera sobre cada número da lista `numeros_teste`
- Em cada iteração, `num` recebe o valor do próximo número

### Linha 34: Chamada da Função
```python
        resultado = eh_primo(num)
```
- Chama a função `eh_primo` passando o número atual
- Armazena o resultado (`True` ou `False`) na variável `resultado`

### Linha 35: Impressão do Resultado
```python
        print(f"{num:3d} é primo? {resultado}")
```
- Usa f-string (string formatada) para exibir o resultado
- **`{num:3d}`**: imprime o número em um espaço de 3 caracteres, alinhado à direita
- **`:3d`**: significa "3 dígitos, formato decimal"
- Imprime cada número testado e sua respectiva resposta

---

## Resumo do Algoritmo

1. ✅ Rejeita números < 2 (não primos)
2. ✅ Aceita 2 (único primo par)
3. ✅ Rejeita números pares > 2
4. ✅ Testa divisibilidade por números ímpares até √n
5. ✅ Se nenhum divisor encontrado, é primo

## Eficiência

- **Complexidade**: O(√n) - muito mais rápido que testar todos os números até n
- **Por quê?**: se um número n tem divisor maior que √n, tem que ter um divisor menor que √n
