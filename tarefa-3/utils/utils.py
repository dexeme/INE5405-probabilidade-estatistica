import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extrai_dados_da_planilha(caminho_planilha, coluna):
    dados = pd.read_excel(caminho_planilha)
    return dados[coluna]

def calcula_resultados(frequencias, n, min_preco, max_preco, k):
    bins = np.linspace(min_preco, max_preco, k + 1)
    xi = (bins[:-1] + bins[1:]) / 2
    Fr = frequencias / n
    xi_fr = xi * Fr
    qdp = ((xi - np.sum(xi_fr))**2) * Fr

    resultados = {
        'xi': xi,
        'qdp': qdp,
        'xi_fr': xi_fr
    }
    return resultados

def calcula_frequencias_e_xi(dados, k):
    intervalos = pd.cut(dados, bins=k, labels=False)
    frequencias = np.bincount(intervalos)
    bins = np.linspace(dados.min(), dados.max(), k + 1)
    xi = (bins[:-1] + bins[1:]) / 2
    return frequencias, xi

def variancia(numeros: list[float]):
    md = np.mean(numeros)
    
    soma_quadrados = sum((x - md) ** 2 for x in numeros)
    
    variancia_resultado = soma_quadrados / len(numeros)
    
    return variancia_resultado

def imprime_estatisticas(estatisticas, titulo="Estatísticas Descritivas"):
    print(f"\n{titulo}:")
    for chave, valor in estatisticas.items():
        print(f"{chave.capitalize()}: {valor:.4f}")

def imprime_erro_relativo(erro_relativo):
    print("\nErro Relativo (%):")
    for chave, valor in erro_relativo.items():
        print(f"{chave.capitalize()}: {valor:.2f}%")

# Atualize a função calcula_estatisticas_descritivas para retornar os dados corretamente
def calcula_estatisticas_descritivas(dados, is_agrupado=False, n=None):
    if is_agrupado:
        media = np.mean(dados['xi'])
        mediana = np.median(dados['xi'])
        variancia_ = np.sum(dados['qdp'])
        desvio_padrao = np.sqrt(variancia_)
        erro_padrao_media = desvio_padrao / np.sqrt(n)
        coef_variacao = (desvio_padrao / np.sum(dados['xi_fr']) ) / 100
    else:
        media = dados.mean()
        mediana = np.median(dados)
        variancia_ = np.var(dados, ddof=1)
        desvio_padrao = np.sqrt(variancia_)
        erro_padrao_media = np.std(dados, ddof=1) / np.sqrt(n)
        coef_variacao = (np.std(dados, ddof=1) / np.mean(dados) ) / 100
    assimetria = (media - mediana) / desvio_padrao if desvio_padrao != 0 else 0

    estatisticas = {
        'media': media,
        'mediana': mediana,
        'variancia': variancia_,
        'desvio_padrao': desvio_padrao,
        'erro_padrao_media': erro_padrao_media,
        'coeficiente_variacao': coef_variacao * 100,  # Para torná-lo percentual
        'assimetria': assimetria
    }
    
    return estatisticas

def gera_histograma(dados, k, cor):
    plt.hist(dados, bins=k, color=cor, edgecolor='black', alpha=0.7)
    plt.title("Histograma por Classe")
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def calcula_erro_relativo(dados_originais, dados_agrupados):
    erro_relativo = {chave: ((dados_originais[chave] - dados_agrupados[chave]) / dados_originais[chave]) * 100 for chave in dados_originais}
    return erro_relativo

def k_metodo_raiz_de_n(dados):
    return round(np.sqrt(len(dados)))

def operacao_principal(caminho_planilha, coluna):
    dados = extrai_dados_da_planilha(caminho_planilha, coluna)
    k = k_metodo_raiz_de_n(dados)
    gera_histograma(dados, k)
    estatisticas_originais = calcula_estatisticas_descritivas(dados)
    print("Estatísticas Descritivas dos Dados Originais:", estatisticas_originais)

    frequencias, xi = calcula_frequencias_e_xi(dados, k)
    estatisticas_agrupadas = calcula_estatisticas_descritivas(xi)
    print("\nEstatísticas Descritivas dos Dados Agrupados:", estatisticas_agrupadas)

    erro_relativo = calcula_erro_relativo(estatisticas_originais, estatisticas_agrupadas)
    print("\nErro Relativo:", erro_relativo)

