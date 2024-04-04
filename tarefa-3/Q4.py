import pandas as pd
from utils import utils
 
#   4-    Compare as medidas básicas descritivas para os dados originais X 
#         dados agrupados, obtendo o erro relativo da perda de informação devido ao agrupamento. 
 

def Q4(caminho_planilha, coluna):
    
    dados = utils.extrai_dados_da_planilha(caminho_planilha, coluna)

    n = len(dados)
    k = utils.k_metodo_raiz_de_n(dados)

    intervalos = pd.cut(dados, bins=k)
    frequencias = intervalos.value_counts().sort_index()
    resultados = utils.calcula_resultados(frequencias, len(dados), min(dados), max(dados), k)

    dados_originais = utils.calcula_estatisticas_descritivas(dados, False, n)
    dados_agrupados = utils.calcula_estatisticas_descritivas(resultados, True, n)
    erro_relativo = utils.calcula_erro_relativo(dados_originais, dados_agrupados)

    utils.imprime_estatisticas(dados_originais, "Estatísticas Descritivas dos Dados Originais")
    utils.imprime_estatisticas(dados_agrupados, "Estatísticas Descritivas dos Dados Agrupados")
    utils.imprime_erro_relativo(erro_relativo)
