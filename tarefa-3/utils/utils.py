from dataclasses import dataclass
from typing import Iterable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

def extrai_dados_da_planilha(caminho_planilha, coluna):
    dados = pd.read_excel(caminho_planilha)
    return dados[coluna]

def calcula_resultados(dados, k):
    intervalos = pd.cut(dados, bins=k, labels=False)
    freq = np.bincount(intervalos)
    freq_acum = np.cumsum(freq)	
    bins = np.linspace(min(dados), max(dados), k + 1)
    xi = (bins[:-1] + bins[1:]) / 2
    amplitude = bins[1] - bins[0]
    Fr = freq / len(dados)
    xi_fr = xi * Fr
    qdp = ((xi - np.sum(xi_fr))**2) * Fr
    intervalo_da_mediana = np.where(freq_acum >= len(dados) / 2)[0][0]
    dados = {
        'intervalo_da_mediana': intervalo_da_mediana,
        'lim_inf_classe': bins[:-1],
        'lim_sup_classe': bins[1:],
        'freq': freq,
        'freq_acum': freq_acum,
        'xi': xi,
        'amplitude': amplitude,
        'qdp': qdp,
        'xi_fr': xi_fr,
    }
    return dados

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
        media = np.mean(sum(dados['freq'] * dados['xi']) / sum(dados['freq']))
        mediana = dados['lim_inf_classe'][dados['intervalo_da_mediana']-1] + ((n/2 - dados['freq_acum'][dados['intervalo_da_mediana']-2]) / dados['freq'][dados['intervalo_da_mediana']-1]) * dados['amplitude']
        variancia_ = ((dados['xi']-media)**2).dot(dados['freq']) / (dados['freq'].sum()-1)
        desvio_padrao = np.sqrt(variancia_)
        erro_padrao_media = desvio_padrao / np.sqrt(n)
        coef_variacao = desvio_padrao / media

        mode_result = st.mode(dados["xi"])
        moda = mode_result.mode if mode_result.count > 1 else "-"
    else:
        media = dados.mean()
        mediana = dados.median()
        variancia_ = dados.var()
        desvio_padrao = np.sqrt(variancia_)
        erro_padrao_media = desvio_padrao / np.sqrt(n)
        coef_variacao = desvio_padrao / media

        mode_result = st.mode(dados)
        moda = mode_result.mode if mode_result.count > 1 else "-"

    assimetria = (media - mediana) / desvio_padrao if desvio_padrao != 0 else 0

    estatisticas = {
        "Classe da Mediana": f"Mediana está na classe {np.where(dados['freq_acum'] >= n / 2)[0][0]}" if is_agrupado else "-",
        "Moda": moda,
        'Média': media,
        'Mediana': mediana,
        'Variância': variancia_,
        'Desvio Padrão': desvio_padrao,
        'Erro Padrão Média': erro_padrao_media,
        'Coeficiente Variação': coef_variacao,
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
            valor = (abs(original - agrupado) / original) * 100
        else:
            valor = "-"
        
        erro_relativo[chave] = valor

    return erro_relativo

def k_metodo_sturges(dados):
    print()
    return round((1 + 3.322 * np.log10(len(dados))))

def k_metodo_raiz_de_n(dados):
    return round(int(np.sqrt(len(dados))))

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
    k = k_metodo_sturges(dados)
    gera_histograma(dados, k)
    estatisticas_originais = calcula_estatisticas_descritivas(dados)
    print("Estatísticas Descritivas dos Dados Originais:", estatisticas_originais)

    dados = calcula_resultados(dados, k)
    estatisticas_agrupadas = calcula_estatisticas_descritivas(dados['xi'])
    print("\nEstatísticas Descritivas dos Dados Agrupados:", estatisticas_agrupadas)

    erro_relativo = calcula_erro_relativo(estatisticas_originais, estatisticas_agrupadas)
    print("\nErro Relativo:", erro_relativo)

