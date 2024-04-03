import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import utils

#  4-    Compare as medidas básicas descritivas para os dados originais X dados agrupados,
#        obtendo o erro relativo da perda de informação devido ao agrupamento. 

coluna = 'I04- PET 500 ML'
caminho_planilha = "C:/Users/dexem/Documents/UFSC/2024.1/probabilidade-estatistica/tarefa-3/dados_seg_1.xlsx"

dados_originais = utils.extrai_dados_da_planilha(caminho_planilha, coluna)
intervalos = pd.cut(dados_originais, bins=13)
dados_agrupados = dados_originais.groupby(intervalos).count()

utils.calcula_estatisticas_descritivas(dados_agrupados)

# Medidas descritivas dos dados originais
media_original = dados_originais.mean()

# Supondo que você represente cada grupo pelo valor médio do grupo nos dados agrupados
media_agrupada = dados_agrupados.mean()

# Cálculo do erro relativo para a média
erro_relativo_media = abs(media_original - media_agrupada) / media_original
erro_relativo_percentual_media = erro_relativo_media * 100

print(f"Erro relativo da média: {erro_relativo_percentual_media}%")