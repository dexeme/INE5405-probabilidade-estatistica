import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


def extrai_dados_da_planilha(caminho_planilha, lista_de_colunas):
    # Carregar a planilha
    dados = pd.read_excel(caminho_planilha)
    dados_especificos = dados[lista_de_colunas]

    print(dados_especificos)
    return dados_especificos

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

def gera_histograma(caminho_planilha, cor, coluna):
    # Carregar a planilha
    dados = extrai_dados_da_planilha(caminho_planilha, coluna)

    # Calcula o número de classes usando o método das raízes -> k = round(sqrt(n))
    n = len(dados)
    k = round(math.sqrt(n))
    
    # Calcula os limites das classes
    intervalos = pd.cut(dados, bins=k, labels=[f"Classe {i+1}" for i in range(k)])
    
    # Conta a frequência de cada classe
    frequencias = intervalos.value_counts().sort_index()
    
    # Calcula os resultados
    calcula_resultados(np.array(frequencias.tolist()), len(dados), dados.min(), dados.max(), k)

    # Plota o histograma
    labels_classes = [f"{i+1}" for i in range(k)]

    plt.figure(figsize=(10, 6))
    plt.bar(labels_classes, frequencias, width=0.5, edgecolor='black', alpha=0.7, color=cor)
    plt.title("Histograma dos Preços dos Isotônicos por Classe")
    plt.xlabel("Classe")
    plt.ylabel("Frequência dos preços")
    plt.grid(axis='y', alpha=0.75)
    plt.show()