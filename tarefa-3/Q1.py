import numpy as np
import pandas as pd
from utils import utils

#   1-    Construa os modelos empíricos (distribuições/tabelas de frequências) 
#         utilizando um critério técnico adequado (raiz de “n” ou Sturges) justificando
#         a escolha para a  situação definida a analisar.

def Q1(caminho_planilha, coluna_a_analisar, cor_do_histograma):
    dados = utils.extrai_dados_da_planilha(caminho_planilha, coluna_a_analisar)
    k = utils.k_metodo_raiz_de_n(dados)
    utils.gera_histograma(dados, k, cor_do_histograma)