# Cálculo do tamanho da amostra usando a fórmula simplificada n_0 = 1 / E^2
# Função para calcular o tamanho da amostra com a fórmula simplificada
def calcular_tamanho_da_amostra_simples(E):
    n_0 = 1 / (E/100)**2
    return n_0

# Função para ajustar o tamanho da amostra para populações finitas
def ajustar_tamanho_da_amostra(n_0, N):
    return round((N * n_0) / (N + n_0))
