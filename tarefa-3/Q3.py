import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import utils

#   3-    Obtenha, dos modelos empíricos, as principais estatísticas descritivas 
#         (valor central: a média, a mediana e a moda (se existir); 
#         dispersão: variância, desvio padrão, erro padrão da média e coeficiente de variação; 
#         forma: assimetria  para analisar as situações desejadas. 

coluna = 'I04- PET 500 ML'
caminho_planilha = "C:/Users/dexem/Documents/UFSC/2024.1/probabilidade-estatistica/tarefa-3/dados_seg_1.xlsx"


dados = utils.extrai_dados_da_planilha(caminho_planilha, coluna)

# Calcula estatísticas para dados originais
print("Estatísticas Descritivas dos Dados Originais:")
utils.calcula_estatisticas_descritivas(dados)

# Calcula estatísticas para xi ponderado
print("\nEstatísticas Descritivas dos Dados Agrupados (xi) Ponderado):")
k = utils.k_metodo_raiz_de_n(dados)
intervalos = pd.cut(dados, bins=k)
frequencias = intervalos.value_counts().sort_index()
xi, qdp, xifr = utils.calcula_resultados(frequencias, len(dados), min(dados), max(dados), k)
utils.calcula_estatisticas_descritivas_agrupados(xi, qdp, xifr)