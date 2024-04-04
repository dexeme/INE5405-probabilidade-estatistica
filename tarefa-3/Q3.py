import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import utils

#   3-    Obtenha, dos modelos empíricos, as principais estatísticas descritivas 
#         (valor central: a média, a mediana e a moda (se existir); 
#         dispersão: variância, desvio padrão, erro padrão da média e coeficiente de variação; 
#         forma: assimetria  para analisar as situações desejadas. 


def Q3(caminho_planilha, coluna):
    dados = utils.extrai_dados_da_planilha(caminho_planilha, coluna)
    k = utils.k_metodo_raiz_de_n(dados)
    n = len(dados)
    intervalos = pd.cut(dados, bins=k)
    frequencias = intervalos.value_counts().sort_index()
    resultados = utils.calcula_resultados(frequencias, len(dados), min(dados), max(dados), k)
    dados_agrupados = utils.calcula_estatisticas_descritivas(resultados, True, n)
    return dados_agrupados


