def calcular_estatisticas_basicas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros (list): Lista de números para análise

    Returns:
        tuple: (soma_total, media, maior_valor, menor_valor)

    Raises:
        ValueError: Se a lista estiver vazia
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia")

    # Calcula a soma total usando função built-in
    soma_total = sum(numeros)

    # Calcula a média
    media = soma_total / len(numeros)

    # Encontra o maior e menor valor usando funções built-in
    maior_valor = max(numeros)
    menor_valor = min(numeros)

    return soma_total, media, maior_valor, menor_valor


# Exemplo de uso
if __name__ == "__main__":
    lista_teste = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    # Chama a função e desempacota os resultados
    total, media, maior, menor = calcular_estatisticas_basicas(lista_teste)

    # Imprime os resultados
    print("Total:", total)
    print("Média:", media)
    print("Maior:", maior)
    print("Menor:", menor)