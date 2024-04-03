import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import utils

#   1-    Construa os modelos empíricos (distribuições/tabelas de frequências) 
#         utilizando um critério técnico adequado (raiz de “n” ou Sturges) justificando
#         a escolha para a  situação definida a analisar.

coluna_de_precos = 'I04- PET 500 ML'
caminho_planilha = "/home/exe/Pessoal/UFSC-2024-1/probabilidade-estatistica/tarefa-3/Planilha (2).xlsx"

utils.gera_histograma(caminho_planilha, 'blue', coluna_de_precos)
utils.gera_histograma(caminho_planilha, 'red', coluna_de_precos)