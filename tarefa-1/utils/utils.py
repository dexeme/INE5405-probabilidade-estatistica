# FUNÇÕES UTILITÁRIAS

# ------------------------ TAREFA 1 ------------------------ #

# Função para calcular a média de uma lista de números
def media(numeros: list[float]):
    return sum(numeros) / len(numeros)

# Função para calcular a mediana de uma lista de números
def mediana(numeros: list[float]):
    # Primeiro, ordenamos a lista de números
    numeros_ordenados = sorted(numeros)
    
    # Verificamos se o número de elementos é ímpar
    if len(numeros_ordenados) % 2 != 0:
        # Se for ímpar, a mediana é o elemento no meio da lista ordenada
        mediana = numeros_ordenados[len(numeros_ordenados) // 2]
    else:
        # Se for par, a mediana é a média dos dois elementos do meio da lista ordenada
        meio_superior = len(numeros_ordenados) // 2
        meio_inferior = meio_superior - 1
        mediana = (numeros_ordenados[meio_inferior] + numeros_ordenados[meio_superior]) / 2
    
    return mediana

# Função para calcular o desvio padrão de uma lista de números
def desvio_padrao(numeros: list[float]):
    md = media(numeros)
    
    soma_quadrados_diferencas = sum((x - md) ** 2 for x in numeros)
    
    variancia = soma_quadrados_diferencas / len(numeros)
    
    desvio_padrao = variancia ** 0.5
    
    return desvio_padrao

# Função para calcular a variância de uma lista de números
def variancia(numeros: list[float]):
    md = media(numeros)
    
    soma_quadrados = sum((x - md) ** 2 for x in numeros)
    
    variancia_resultado = soma_quadrados / len(numeros)
    
    return variancia_resultado

# Função para calcular o coeficiente de variação de uma lista de números
def coeficiente_variacao(numeros: list[float]):
    dp = desvio_padrao(numeros)
    
    md = media(numeros)
    
    coeficiente_variacao = (dp / md)
    
    return coeficiente_variacao

# ----------------------------------------------------------- #