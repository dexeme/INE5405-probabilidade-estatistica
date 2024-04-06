from dataclasses import dataclass
from typing import Iterable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

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
    print(numeros)
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

        mode_result = st.mode(dados["xi"])
        moda = mode_result.mode if mode_result.count > 1 else "-"
    else:   
        
        print("dados", dados)
        media = np.mean(dados)
        mediana = np.median(dados)
        variancia_ = np.var(np.array(dados))
        desvio_padrao = np.sqrt(variancia_)
        erro_padrao_media = desvio_padrao / np.sqrt(n)
        coef_variacao = desvio_padrao / media

        mode_result = st.mode(dados)
        moda = mode_result.mode if mode_result.count > 1 else "-"

    assimetria = (media - mediana) / desvio_padrao if desvio_padrao != 0 else 0

    estatisticas = {
        "Moda": moda,
        'Média': media,
        'Mediana': mediana,
        'Variância': variancia_,
        'Desvio Padrão': desvio_padrao,
        'Erro Padrão Média': erro_padrao_media,
        'Coeficiente Variação': coef_variacao * 100,  # Para torná-lo percentual
        'Assimetria': assimetria
    }
    
    return estatisticas

def gera_histograma(dados, k, cor, titulo):
    intervalos = calcula_intervalos_de_classe(dados, k)
    ticks = [*(menor for (menor, _) in intervalos), intervalos[-1][1]]

    plt.hist(dados, bins=k, color=cor, edgecolor='black', alpha=0.7)
    plt.xticks(ticks)
    plt.title(titulo)
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.grid(axis='y', alpha=0.75)
    plt.show()


def gera_boxplot(dados, titulo, cor):
    plot = plt.boxplot(dados, notch=True, patch_artist=True)

    for patch in plot["boxes"]:
        patch.set_facecolor(cor)

    plt.title(titulo)
    plt.ylabel("Preços")
    plt.show()

def calcula_erro_relativo(dados_originais, dados_agrupados):
    erro_relativo = {}

    for chave in dados_originais:
        original = dados_originais[chave]
        agrupado = dados_agrupados[chave]

        if isinstance(original, float) and isinstance(agrupado, float):
            valor = ((original - agrupado) / original) * 100
        else:
            valor = "-"
        
        erro_relativo[chave] = valor

    return erro_relativo

def k_metodo_raiz_de_n(dados):
    return round(np.sqrt(len(dados)))

def calcula_intervalos_de_classe(dados: Iterable[float], k: int) -> list[tuple[float, float]]:
    menor = min(dados)
    maior = max(dados)
    extensao = (maior - menor) / k

    return [
        (menor + i*extensao, menor + (i + 1)*extensao)
        for i in range(k)
    ]

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

