import math
import numpy as np
from utils.utils import extrai_dados_da_planilha, gera_boxplot

def Q5(caminho_planilha, coluna, titulo_plot, cor_plot):
    dados = extrai_dados_da_planilha(caminho_planilha, coluna)

    n = len(dados)
    menor = min(dados)
    maior = max(dados)

    dados_ord = sorted(dados)
    primeiro_quartil = dados_ord[math.ceil(n/4)]
    terceiro_quartil = dados_ord[math.ceil(n * 3/4)]
    mediana = np.median(dados)
    iqr = terceiro_quartil - primeiro_quartil

    print(f"Menor: {menor}")
    print(f"1º Quartil: {primeiro_quartil}")
    print(f"Mediana: {mediana}")
    print(f"3º Quartil: {terceiro_quartil}")
    print(f"Maior: {maior}")
    print(f"IQR: {iqr}")

    gera_boxplot(dados, titulo_plot, cor_plot)