import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def calcula_resultados(frequencias):
    n = 174  # Total de observações fornecido

    # Calcular a frequência relativa (Fr) para cada classe
    Fr = frequencias / n

    # Calcula a frequência acumulada
    frequencia_acumulada = np.cumsum(frequencias)

    # Calcula a frequência relativa (Fr) baseada na frequência acumulada
    #Fr = frequencia_acumulada / n

    # Supõe que os limites das classes são conhecidos
    min_preco, max_preco = 4.5, 8.9
    classes = len(frequencias)
    bins = np.linspace(min_preco, max_preco, classes + 1)

    # Calcula xi (ponto médio) para cada classe
    xi = (bins[:-1] + bins[1:]) / 2

    # Calcula xi * Fr para cada classe
    xi_fr = xi * Fr

    # Calcula o QDP (quadrado da diferença dos pontos médios) para cada classe
    #=POW(W31-X44;2) * V31
    qdp = ((xi - np.sum(xi_fr))**2) * Fr


    # Prepara os resultados para exibição
    resultados = pd.DataFrame({
        'Classe': [f"Classe {i+1}" for i in range(classes)],
        'Frequência': frequencias,
        'Frequência Acumulada': frequencia_acumulada,
        'Fr': Fr,
        'xi': xi,
        'xi*Fr': xi_fr,
        'QDP': qdp
    })

    # Calcula o QDP (considerando que a soma de todos os xi*Fr já é o valor ajustado)
    soma_xi_fr = np.sum(xi * (frequencias / n))  # Utiliza frequências não acumuladas para calcular xi*fr
    primeiro_xi = xi[0]
    primeiro_fr = Fr[0]
    QDP = (primeiro_xi - soma_xi_fr) * primeiro_fr

    print(resultados)
    print(f"\nQDP: {QDP}")

def processar_isotonicos(caminho_planilha):
    # Carregar a planilha
    dados = pd.read_excel(caminho_planilha)
    
    # Assume que a última coluna contém os preços dos isotônicos
    precos_isotonico = dados.iloc[:, -1].dropna()  # Remove NaNs
    
    # Calcula o número de classes usando o método das raízes
    n = len(precos_isotonico)
    k = round(math.sqrt(n))
    
    intervalos = pd.cut(precos_isotonico, bins=k, labels=[f"Classe {i+1}" for i in range(k)])
    
    # Conta a frequência de cada classe
    frequencias = intervalos.value_counts().sort_index()
    lista_de_frequencias = frequencias.tolist()
    
    # Calcula os resultados
    calcula_resultados(np.array(lista_de_frequencias))
    
    # Exibe a tabela de frequências
    print("Tabela de Frequências dos Preços dos Isotônicos:")
    print(frequencias)
    classes = len(frequencias)
    # Prepara os rótulos para o eixo X
    labels_classes = [f"{i+1}" for i in range(classes)]
    # Plotagem do histograma com rótulos personalizados no eixo X
    plt.figure(figsize=(10, 6))
    plt.bar(labels_classes, frequencias, width=0.5, edgecolor='black', alpha=0.7, color='green')
    plt.title("Histograma dos Preços dos Isotônicos por Classe")
    plt.xlabel("Classe")
    plt.ylabel("Frequência dos preços")
    plt.grid(axis='y', alpha=0.75)
    plt.show()

processar_isotonicos("C:/Users/dexem/Documents/UFSC/2024.1/probabilidade-estatistica/tarefa-3/dados_seg_2.xlsx")
