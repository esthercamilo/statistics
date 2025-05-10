import numpy as np
import matplotlib.pyplot as plt

def calcula_probabilidade_doenca(tamanho_grupo, incidencia, falso_positivo):
    """
    Calcula a probabilidade de uma pessoa com teste positivo realmente ter a doença.

    Args:
        tamanho_grupo (int): O número de pessoas no grupo.
        incidencia (float): A incidência da doença na população (entre 0 e 1).
        falso_positivo (float): A taxa de falso positivo do teste (entre 0 e 1).

    Returns:
        float: A probabilidade de uma pessoa com teste positivo realmente ter a doença.
    """
    num_doentes = int(tamanho_grupo * incidencia)
    num_nao_doentes = tamanho_grupo - num_doentes

    positivos_verdadeiros = num_doentes
    positivos_falsos = round(num_nao_doentes * falso_positivo)

    total_positivos = positivos_verdadeiros + positivos_falsos

    if total_positivos == 0:
        return 0.0  # Evita divisão por zero

    probabilidade = positivos_verdadeiros / total_positivos
    return probabilidade

# Definindo os parâmetros
incidencia_doenca = 0.01  # 1%
taxa_falso_positivo = 0.05  # 5%
tamanhos_grupos = [100, 1000, 10000, 100000]
probabilidades = []

# Calculando as probabilidades para diferentes tamanhos de grupo
for tamanho in tamanhos_grupos:
    prob = calcula_probabilidade_doenca(tamanho, incidencia_doenca, taxa_falso_positivo)
    probabilidades.append(prob)
    print(f"Em um grupo de {tamanho} pessoas, a probabilidade de alguém com teste positivo estar doente é de: {prob:.4f}")

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(tamanhos_grupos, probabilidades, marker='o')
plt.xlabel("Tamanho do Grupo")
plt.ylabel("Probabilidade de Doença Dado Teste Positivo")
plt.title("Probabilidade de Doença vs. Tamanho do Grupo")
plt.grid(True)
plt.xticks(tamanhos_grupos)
plt.yticks(np.arange(0, 0.3, 0.02)) # Ajustando os limites do eixo y para melhor visualização
plt.savefig('plots/disease.png')

