import numpy as np
import pandas as pd
from utils.utils import calcula_intervalos_de_classe, extrai_dados_da_planilha, k_metodo_sturges, gera_histograma, k_metodo_raiz_de_n

#   1-    Construa os modelos empíricos (distribuições/tabelas de frequências) 
#         utilizando um critério técnico adequado (raiz de “n” ou Sturges) justificando
#         a escolha para a  situação definida a analisar.

def Q1(caminho_planilha, coluna_a_analisar, cor_do_histograma, titulo_do_histograma):
    dados = extrai_dados_da_planilha(caminho_planilha, coluna_a_analisar)

    N = len(dados)
    print(f"N: {N}")

    menor = min(dados)
    maior = max(dados)
    print(f"Intervalo: [{menor}, {maior}]")

    extensao = maior - menor
    print(f"Extensão: {extensao}")

    k = k_metodo_sturges(dados)
    intervalo_classes = calcula_intervalos_de_classe(dados, k)
    frequencia = [len([v for v in dados if inf <= v <= sup]) for inf, sup in intervalo_classes]
    Fr = [freq / N for freq in frequencia]
    Xi = [(inf + sup) / 2 for inf, sup in intervalo_classes]
    Xi_Fr = [x * f for x, f in zip(Xi, Fr)]
    sum_Xi_Fr = sum(Xi_Fr)
    qdp = [(x - sum_Xi_Fr)**2 * f for x, f in zip(Xi, Fr)]

    tabela_frequencias = pd.DataFrame({
        "Classe": range(1, k+1),
        "L. Inferior": [inf for inf, _ in intervalo_classes],
        "L. Superior": [sup for _, sup in intervalo_classes],
        "Extensão": [sup - inf for inf, sup in intervalo_classes],
        "Frequência": frequencia,
        "Fr": Fr,
        "Xi": Xi,
        "Xi * Fr": Xi_Fr,
        "QDP": qdp,
    })
    print(tabela_frequencias)

    caminho_tabela = input("Caminho de destino da tabela acima (Branco para ignorar): ")
    if caminho_tabela:
        if "." not in caminho_tabela:
            caminho_tabela = caminho_tabela + ".xlsx"

        tabela_frequencias.to_excel(caminho_tabela, index=False)
        print(f"Tabela salva em '{caminho_tabela}'")

    gera_histograma(dados, k, cor_do_histograma, titulo_do_histograma)