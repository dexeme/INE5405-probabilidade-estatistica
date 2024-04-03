import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import variation


def extrai_dados_da_planilha(caminho_planilha, coluna):
    dados = pd.read_excel(caminho_planilha)
    return dados[coluna]

def calcula_resultados(frequencias, n, min_preco, max_preco, k):
    # Calcular a frequência relativa (Fr) para cada classe
    Fr = frequencias / n

    # Calcula a frequência acumulada
    frequencia_acumulada = np.cumsum(frequencias)

    # Calcula a frequência relativa (Fr) baseada na frequência acumulada
    # Fr = frequencia_acumulada / n

    # Supõe que os limites das classes são conhecidos
    bins = np.linspace(min_preco, max_preco, k + 1)

    # Calcula xi (ponto médio) para cada classe
    xi = (bins[:-1] + bins[1:]) / 2

    # Calcula xi * Fr para cada classe
    xi_fr = xi * Fr

    # Calcula o QDP (quadrado da diferença dos pontos médios) para cada classe
    # = ((xi-xi_fr)²) * fr
    qdp = ((xi - np.sum(xi_fr))**2) * Fr

    # Prepara os resultados para exibição
    resultados = pd.DataFrame({
        'Classe': [f"Classe {i+1}" for i in range(k)],
        'Frequência': frequencias,
        'Frequência Acumulada': frequencia_acumulada,
        'Fr': Fr,
        'xi': xi,
        'xi*Fr': xi_fr,
        'QDP': qdp
    })

    print(resultados)
    return xi, qdp, xi_fr

def gera_histograma(dados, cor, k):
    intervalos = pd.cut(dados, bins=k, labels=[f"Classe {i+1}" for i in range(k)])
    frequencias = intervalos.value_counts().sort_index()

    labels_classes = [f"{i+1}" for i in range(k)]
    plt.figure(figsize=(10, 6))
    plt.bar(labels_classes, frequencias, width=0.5, edgecolor='black', alpha=0.7, color=cor)
    plt.title("Histograma por Classe")
    plt.xlabel("Classe")
    plt.ylabel("Frequência")
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    
    return np.array(frequencias.tolist())

def variancia(numeros: list[float]):
    md = np.mean(numeros)
    
    soma_quadrados = sum((x - md) ** 2 for x in numeros)
    
    variancia_resultado = soma_quadrados / len(numeros)
    
    return variancia_resultado

def calcula_estatisticas_descritivas_agrupados(dados, qdp, xifr):
    
    media = dados.mean()
    mediana = np.median(dados)
    try:
        moda = dados.mode()[0]
    except:
        moda = "Não existe"
    variancia_ = np.sum(qdp)
    desvio_padrao = np.sqrt(variancia_)
    erro_padrao_media = desvio_padrao / math.sqrt(220)
    coeficiente_variacao = desvio_padrao / np.sum(xifr)
    assimetria = (media - mediana) / desvio_padrao

    print(f"DADOS AGRUPADOS")
    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Variância: {variancia_}")
    print(f"Desvio Padrão: {desvio_padrao}")
    print(f"Erro Padrão da Média: {erro_padrao_media}")
    print(f"Coeficiente de Variação: {coeficiente_variacao}")
    print(f"Assimetria: {assimetria}")

def calcula_estatisticas_descritivas(dados):
    print("Estatísticas Descritivas:")
    media = dados.mean()
    mediana = np.median(dados)
    try:
        moda = dados.mode()[0]
    except:
        moda = "Não existe"
    variancia_ = variancia(dados)
    desvio_padrao = np.sqrt(variancia_)
    erro_padrao_media = np.std(dados, ddof=1) / np.sqrt(len(dados))
    coeficiente_variacao = np.std(dados, ddof=1) / np.mean(dados)
    assimetria = (media - mediana) / desvio_padrao

    print(f"DADOS ORIGINAIS")
    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Variância: {variancia_}")
    print(f"Desvio Padrão: {desvio_padrao}")
    print(f"Erro Padrão da Média: {erro_padrao_media}")
    print(f"Coeficiente de Variação: {coeficiente_variacao}")
    print(f"Assimetria: {assimetria}")


def k_metodo_raiz_de_n(dados):
    return round(np.sqrt(len(dados)))