# Explicação Linha a Linha - Verificador de Números Primos

## Definição da Função

```python
def eh_primo(numero):
```
- **`def`**: Palavra-chave Python para definir uma função
- **`eh_primo`**: Nome da função
- **`(numero)`**: Parâmetro que a função recebe (o número a ser verificado)

## Docstring (Documentação)

```python
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
```
- **Docstring**: Texto entre `"""` que documenta a função
- **Descreve**: O que a função faz, quais parâmetros recebe e o que retorna
- **Útil para**: Entender rapidamente como usar a função

## Primeira Verificação: Números Menores que 2

```python
    if numero < 2:
        return False
```
- **`if numero < 2:`**: Verifica se o número é menor que 2
- **Por quê?**: Números negativos, zero e 1 NÃO são primos por definição matemática
- **`return False`**: Retorna falso (não é primo) e encerra a função

## Segunda Verificação: Número 2

```python
    if numero == 2:
        return True
```
- **`if numero == 2:`**: Verifica se o número é exatamente 2
- **Por quê?**: 2 é o ÚNICO número primo par
- **`return True`**: Retorna verdadeiro (é primo)

## Terceira Verificação: Números Pares

```python
    if numero % 2 == 0:
        return False
```
- **`numero % 2`**: Operador `%` (módulo) retorna o resto da divisão
- **`== 0`**: Se o resto é zero, o número é par
- **Por quê?**: Todo número par (exceto 2, já verificado) é divisível por 2, logo não é primo
- **`return False`**: Retorna falso (não é primo)

## Loop Principal - Verificação de Divisibilidade

```python
    for i in range(3, int(numero**0.5) + 1, 2):
```
- **`for i in`**: Começa um loop que passa por cada valor de `i`
- **`range(3, int(numero**0.5) + 1, 2)`**: Gera números de 3 até a raiz quadrada
  - **`3`**: Começa em 3 (já verificamos 2)
  - **`numero**0.5`**: `**` é exponenciação; `0.5` é a mesma coisa que raiz quadrada
  - **`int(...)`**: Converte para número inteiro
  - **`+ 1`**: Adiciona 1 para incluir o último número
  - **`2`**: Incrementa de 2 em 2 (só verifica números ímpares)

### Exemplo Prático
Se `numero = 25`:
- `25**0.5 = 5`
- `range(3, 6, 2)` gera: `3, 5`
- Testa divisibilidade por 3 e por 5

### Por quê até a raiz quadrada?
- Se um número tem um divisor maior que sua raiz quadrada, também terá um divisor menor
- Isso torna o algoritmo muito mais eficiente! ⚡

## Verificação de Divisibilidade

```python
        if numero % i == 0:
            return False
```
- **`numero % i == 0`**: Verifica se `i` divide `numero` sem resto
- **Se verdadeiro**: Encontramos um divisor, então o número NÃO é primo
- **`return False`**: Encerra a função imediatamente

## Resultado Final

```python
    return True
```
- Se nenhum divisor foi encontrado no loop, o número é primo
- **`return True`**: O número é primo!

---

## Seção de Exemplos

```python
if __name__ == "__main__":
```
- **`if __name__ == "__main__":`**: Verificação especial do Python
- **Significado**: Executa este bloco apenas se o arquivo é executado diretamente
- **Não executa**: Se o arquivo é importado em outro script

## Loop de Testes

```python
    numeros_teste = [1, 2, 3, 4, 5, 10, 11, 17, 20, 23, 97]
```
- **`[...]`**: Lista com vários números para testar
- Inclui: números pequenos, pares, ímpares e primos

## Exibição de Resultados

```python
    print("Verificando números primos:\n")
```
- **`print(...)`**: Exibe texto na tela
- **`\n`**: Caractere de quebra de linha (espaço em branco)

## Loop de Impressão

```python
    for num in numeros_teste:
        resultado = eh_primo(num)
        print(f"{num:3d} é primo? {resultado}")
```

1. **`for num in numeros_teste:`**: Passa por cada número da lista
2. **`resultado = eh_primo(num)`**: Chama a função e armazena o resultado
3. **`print(f"...")`**: `f-string` (string formatada) exibe o resultado
   - **`{num:3d}`**: Exibe o número com 3 espaços de largura
   - **`{resultado}`**: Exibe True ou False

### Exemplo de Saída
```
Verificando números primos:

  1 é primo? False
  2 é primo? True
  3 é primo? True
  4 é primo? False
  5 é primo? True
```

---

## Resumo da Eficiência 🚀

O algoritmo é eficiente porque:
1. ✅ Descarta números pares rapidamente
2. ✅ Só verifica até a raiz quadrada
3. ✅ Só verifica números ímpares no loop
4. ✅ Retorna False imediatamente ao encontrar um divisor
