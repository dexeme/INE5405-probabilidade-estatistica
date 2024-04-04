import os
import pandas as pd
import numpy as np
from utils import utils
from Q1 import Q1
from Q3 import Q3
from Q4 import Q4

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Filtragem de informações numa planilha")
        print("2. Escolher uma planilha filtrada")
        print("3. Sair")
        
        escolha = input("Digite a opção desejada: ")
        
        if escolha == '1':
            print("Filtragem (ainda não implementada)")
        elif escolha == '2':
            caminho_planilha = escolher_planilha("planilhas")
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
        print("4. Executar todas as operações")
        print("5. Voltar ao menu principal")
        
        escolha = input("Selecione a operação desejada: ")
        
        if escolha == '1':
            # Substitua 'funcao_Q1' pelo nome real da sua função
            cor_histograma = escolher_cor()
            Q1(caminho_planilha, coluna_a_analisar, cor_histograma)
        elif escolha == '2':
            # Substitua 'funcao_Q2' pelo nome real da sua função
            Q3(caminho_planilha, coluna_a_analisar)
        elif escolha == '3':
            # Substitua 'funcao_Q3' pelo nome real da sua função
            Q4(caminho_planilha, coluna_a_analisar)
        elif escolha == '4':
            # Substitua pelos nomes reais das suas funções
            cor_histograma = escolher_cor()
            Q1(caminho_planilha, coluna_a_analisar, cor_histograma)
            Q3(caminho_planilha, coluna_a_analisar)
            Q4(caminho_planilha, coluna_a_analisar)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()