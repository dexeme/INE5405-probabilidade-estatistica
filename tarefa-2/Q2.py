from utils import utils

# Tamanho da população
N = 8000

# Porcentagens de teste
porcentagens = [4.0, 4.5, 5.0]

valor = [utils.calcular_tamanho_da_amostra_simples(E) for E in porcentagens]
valor_ajustado = [utils.ajustar_tamanho_da_amostra(n_0, N) for n_0 in valor]
print(valor)
print(valor_ajustado)