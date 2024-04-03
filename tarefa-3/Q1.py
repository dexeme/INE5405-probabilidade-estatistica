import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import utils

#   1-    Construa os modelos empíricos (distribuições/tabelas de frequências) 
#         utilizando um critério técnico adequado (raiz de “n” ou Sturges) justificando
#         a escolha para a  situação definida a analisar.

coluna_de_precos = 'I04- PET 500 ML'
caminho_planilha = "C:/Users/dexem/Documents/UFSC/2024.1/probabilidade-estatistica/tarefa-3/dados_seg_1.xlsx"

dados = utils.extrai_dados_da_planilha(caminho_planilha, coluna_de_precos)
n = len(dados)
k = round(np.sqrt(n))
utils.gera_histograma(dados, 'blue', k)
