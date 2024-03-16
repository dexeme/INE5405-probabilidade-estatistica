import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import utils

# Data for Gasolina Aditivada
data_aditivada = {
    'ESTADO': ['TOCANTINS', 'RIO GRANDE DO SUL', 'RONDONIA', 'PERNAMBUCO', 'ACRE', 'RIO DE JANEIRO', 'BAHIA', 'MARANHAO', 'SAO PAULO', 'PIAUI'],
    'MUNICIPIO': ['PALMAS', 'PORTO ALEGRE', 'PORTO VELHO', 'RECIFE', 'RIO BRANCO', 'RIO DE JANEIRO', 'SALVADOR', 'SAO LUIS', 'SAO PAULO', 'TERESINA'],
    'PRODUTO': ['GASOLINA ADITIVADA'] * 10,
    'NUMERO_DE_POSTOS_PESQUISADOS': [13, 32, 9, 19, 12, 72, 1, 13, 184, 23],
    'UNIDADE_DE_MEDIDA': ['R$/l'] * 10,
    'PRECO_MEDIO_REVENDA': [6.06, 5.79, 6.44, 5.75, 6.80, 5.82, 6.29, 5.36, 5.99, 5.78],
    'DESVIO_PADRAO_REVENDA': [0.132, 0.231, 0.112, 0.093, 0.095, 0.283, 0.000, 0.201, 0.683, 0.203],
    'PRECO_MINIMO_REVENDA': [5.95, 5.45, 6.28, 5.56, 6.69, 5.29, 6.29, 5.18, 4.99, 5.39],
    'PRECO_MAXIMO_REVENDA': [6.36, 6.29, 6.65, 5.96, 6.98, 6.78, 6.29, 5.69, 7.99, 5.99],
    'COEF_DE_VARIACAO_REVENDA': [0.022, 0.040, 0.017, 0.016, 0.014, 0.049, 0.000, 0.038, 0.114, 0.035]
}

# Data for Gasolina Comum
data_comum = {
    'ESTADO': ['TOCANTINS', 'RIO GRANDE DO SUL', 'RONDONIA', 'PERNAMBUCO', 'ACRE', 'RIO DE JANEIRO', 'BAHIA', 'MARANHAO', 'SAO PAULO', 'PIAUI'],
    'MUNICIPIO': ['PALMAS', 'PORTO ALEGRE', 'PORTO VELHO', 'RECIFE', 'RIO BRANCO', 'RIO DE JANEIRO', 'SALVADOR', 'SAO LUIS', 'SAO PAULO', 'TERESINA'],
    'PRODUTO': ['GASOLINA COMUM'] * 10,
    'NUMERO_DE_POSTOS_PESQUISADOS': [14, 33, 19, 27, 14, 68, 1, 20, 180, 28],
    'UNIDADE_DE_MEDIDA': ['R$/l'] * 10,
    'PRECO_MEDIO_REVENDA': [5.96, 5.61, 6.33, 5.61, 6.74, 5.57, 5.79, 5.19, 5.64, 5.54],
    'DESVIO_PADRAO_REVENDA': [0.009, 0.134, 0.166, 0.054, 0.054, 0.226, 0.000, 0.072, 0.643, 0.142],
    'PRECO_MINIMO_REVENDA': [5.95, 5.38, 5.89, 5.54, 6.69, 5.09, 5.79, 5.03, 4.69, 5.39],
    'PRECO_MAXIMO_REVENDA': [5.98, 5.89, 6.49, 5.69, 6.86, 6.29, 5.79, 5.29, 7.97, 5.99],
    'COEF_DE_VARIACAO_REVENDA': [0.002, 0.024, 0.026, 0.010, 0.008, 0.040, 0.000, 0.014, 0.114, 0.026]
}

# Convert to DataFrame
df_aditivada = pd.DataFrame(data_aditivada)
df_comum = pd.DataFrame(data_comum)

# Calculating the required statistics
mean_aditivada = utils.media(df_aditivada['PRECO_MEDIO_REVENDA'])
median_aditivada = utils.mediana(df_aditivada['PRECO_MEDIO_REVENDA'])
variance_aditivada = utils.variancia(df_aditivada['PRECO_MEDIO_REVENDA'])
std_dev_aditivada = utils.desvio_padrao(df_aditivada['PRECO_MEDIO_REVENDA'])
coef_var_aditivada = utils.coeficiente_variacao(df_aditivada['PRECO_MEDIO_REVENDA'])

mean_comum = utils.media(df_comum['PRECO_MEDIO_REVENDA'])
median_comum = utils.mediana(df_comum['PRECO_MEDIO_REVENDA'])
variance_comum = utils.variancia(df_comum['PRECO_MEDIO_REVENDA'])
std_dev_comum = utils.desvio_padrao(df_comum['PRECO_MEDIO_REVENDA'])
coef_var_comum = utils.coeficiente_variacao(df_comum['PRECO_MEDIO_REVENDA'])

# Prepare the results for display
results = {
    "Média Aditivada": mean_aditivada,
    "Média Comum": mean_comum,
    "Mediana Aditivada": median_aditivada,
    "Mediana Comum": median_comum,
    "Variância Aditivada": variance_aditivada,
    "Variância Comum": variance_comum,
    "Desvio Padrão Aditivada": std_dev_aditivada,
    "Desvio Padrão Comum": std_dev_comum,
    "Coeficiente de Variação Aditivada": coef_var_aditivada,
    "Coeficiente de Variação Comum": coef_var_comum
}

# Create the comparative dot plot
plt.figure(figsize=(12, 7))

# Plotting the comparative dot plot

# Gasolina Aditivada
plt.scatter(df_aditivada['MUNICIPIO'], df_aditivada['PRECO_MEDIO_REVENDA'], color='blue', label='Gasolina Aditivada')
# Gasolina Comum
plt.scatter(df_comum['MUNICIPIO'], df_comum['PRECO_MEDIO_REVENDA'], color='red', label='Gasolina Comum')

plt.xlabel('Município')
plt.ylabel('Preço Médio Revenda (R$/L)')
plt.title('Comparação de Preços de Gasolina Aditivada e Comum')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()

# Save the plot to a file
plot_filename = './result/comparative_dot_plot.png'
plt.savefig(plot_filename)
plt.close()
print(results)
plot_filename, results
