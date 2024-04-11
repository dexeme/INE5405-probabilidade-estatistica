import pandas as pd
from utils import utils
 
#   4-    Compare as medidas básicas descritivas para os dados originais X 
#         dados agrupados, obtendo o erro relativo da perda de informação devido ao agrupamento. 
 

def Q4(caminho_planilha, coluna, k_metodo):
    
    dados = utils.extrai_dados_da_planilha(caminho_planilha, coluna)

    n = len(dados)
    k = k_metodo(dados)

    resultados = utils.calcula_resultados(dados, k)

    dados_originais = utils.calcula_estatisticas_descritivas(dados, False, n)
    dados_agrupados = utils.calcula_estatisticas_descritivas(resultados, True, n)
    erro_relativo = utils.calcula_erro_relativo(dados_originais, dados_agrupados)

    tabela = pd.DataFrame({
        "-": dados_originais.keys(),
        "Agrupados": dados_agrupados.values(),
        "Não Agrupados": dados_originais.values(),
        "Erro Relativo": erro_relativo.values(),
    })
    print(tabela)

    caminho = input("Caminho da tabela acima (Branco para ignorar): ")
    if caminho:
        tabela.to_excel(caminho if "." in caminho else f"{caminho}.xlsx", index=False)
