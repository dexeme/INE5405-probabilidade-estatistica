import os
import pandas as pd
import numpy as np
from utils import utils
from Q1 import Q1
from Q3 import Q3
from Q4 import Q4
from Q5 import Q5

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Filtragem de informações numa planilha")
        print("2. Escolher uma planilha filtrada")
        print("3. Sair")
        
        escolha = input("Digite a opção desejada: ")
        
        if escolha == '1':
            caminho_planilha = escolher_planilha("planilhas")
            if caminho_planilha:
                extrai_dados_da_planilha_completa(caminho_planilha)
        elif escolha == '2':
            caminho_planilha = escolher_planilha("planilhas_extraidas")
            if caminho_planilha:
                menu_operacoes_na_planilha(caminho_planilha)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def escolher_planilha(diretorio):
    arquivos = [arq for arq in os.listdir(diretorio) if arq.endswith('.xlsx')]
    for indice, arquivo in enumerate(arquivos, start=1):
        print(f"{indice}. {arquivo}")
    
    escolha = int(input("Selecione uma planilha pelo número: "))
    caminho_planilha = os.path.join(diretorio, arquivos[escolha - 1])
    print(f"Planilha selecionada: {caminho_planilha}")
    
    return caminho_planilha

def escolher_coluna(caminho_planilha):
    # Carrega apenas as colunas (não os dados) para economizar memória
    colunas = pd.read_excel(caminho_planilha, nrows=0).columns.tolist()
    print("\nColunas disponíveis:")
    for indice, coluna in enumerate(colunas, start=1):
        print(f"{indice}. {coluna}")
    
    escolha = int(input("Selecione uma coluna pelo número: "))
    coluna_escolhida = colunas[escolha - 1]
    print(f"Coluna selecionada: {coluna_escolhida}")
    
    return coluna_escolhida

def escolher_titulo(default="Title"):
    titulo = input("Título do plot: ")
    return titulo if titulo.strip() else default

def escolher_cor():
    print("\nCores disponíveis:")
    print("1. Azul")
    print("2. Vermelho")
    print("3. Verde")
    print("4. Rosa")
    print("5. Preto")
    
    escolha = input("Selecione uma cor pelo número: ")
    if escolha == '1':
        return 'blue'
    elif escolha == '2':
        return 'red'
    elif escolha == '3':
        return 'green'
    elif escolha == '4':
        return 'pink'
    elif escolha == '5':
        return 'black'
    else:
        print("Cor inválida. Usando azul como padrão.")
        return 'blue'

def menu_operacoes_na_planilha(caminho_planilha):
    coluna_a_analisar = escolher_coluna(caminho_planilha)
    while True:
        print("\nOperações na Planilha:")
        print("1. Executar Q1")
        print("2. Executar Q3")
        print("3. Executar Q4")
        print("4. Executar Q5")
        print("5. Executar todas as operações")
        print("6. Voltar ao menu principal")
        
        escolha = input("Selecione a operação desejada: ")
        
        if escolha == '1':
            cor_histograma = escolher_cor()
            titulo_histograma = escolher_titulo("Histograma por Classe")
            Q1(caminho_planilha, coluna_a_analisar, cor_histograma, titulo_histograma)
        elif escolha == '2':
            Q3(caminho_planilha, coluna_a_analisar)
        elif escolha == '3':
            Q4(caminho_planilha, coluna_a_analisar)
        elif escolha == '4':
            cor_plot = escolher_cor()
            titulo_plot = escolher_titulo("Boxplot")
            Q5(caminho_planilha, coluna_a_analisar, titulo_plot, cor_plot)
        elif escolha == '5':
            cor_histograma = escolher_cor()
            titulo_histograma = escolher_titulo("Histograma por Classe")
            Q1(caminho_planilha, coluna_a_analisar, cor_histograma, titulo_histograma)
            Q3(caminho_planilha, coluna_a_analisar)
            Q4(caminho_planilha, coluna_a_analisar)
            cor_plot = escolher_cor()
            titulo_plot = escolher_titulo("Boxplot")
            Q5(caminho_planilha, coluna_a_analisar, titulo_plot, cor_plot)
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

def filtrar_por_valor_de_coluna(criterio: str, valores: np.ndarray, indice_coluna: int) -> np.ndarray:
    return valores[valores[:, indice_coluna] == criterio]

def prompt_items(prompt: str, items: list) -> int:
    print(prompt + " " + ", ".join(items))
    return int(input("Escolha o índice da coluna desejada: "))

def extrai_dados_da_planilha_completa(caminho_planilha:str) -> np.ndarray:
    # Carregar a planilha
    tabela = pd.read_excel(caminho_planilha)

    valores = tabela.values

    valores_produto = filtrar_por_valor_de_coluna("Produtos: ", valores, 0)
    valores_marca = filtrar_por_valor_de_coluna("Marcas: ", valores_produto, 7)

    embalagem_i = prompt_items("Embalagens: ", tabela.columns[8:]) + 8
    valores_filtrados = valores_marca[~pd.isnull(valores_marca[:, embalagem_i])]

    seg = None
    while seg not in ("1", "2"):
        seg = input("Segmento (1, 2): ")

    segmento = valores_filtrados[valores_filtrados[:, 3] == int(seg)]

    output_file = input("Nome do arquivo de saída (enter para deixar padrão): ")
    tabela_filtrada = pd.DataFrame({
        label: segmento[:, i] for i, label in enumerate(tabela.columns)
    })
    
    if output_file != "":
        caminho_completo = f"planilhas_extraidas/" + output_file + ".xlsx"
    else:
        caminho_completo = "planilhas_extraidas/tabela_filtrada.xlsx"

    # Salvando o DataFrame com o formato especificado para números flutuantes
    tabela_filtrada.to_excel(caminho_completo, float_format="%.4f", index=False, excel_writer="xlsxwriter")

    dados = segmento[:, embalagem_i]
    return dados

if __name__ == "__main__":
    menu_principal()