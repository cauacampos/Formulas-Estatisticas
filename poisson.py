from scipy.stats import poisson

"""Média de acidentes de carro por dia = 2"""

# Qual a probabilidade de ocorrerem 3 acidentes no dia
float(poisson.pmf(3, 2))

# Qual a probabilidade de ocorrerem 3 ou menos acidentes no dia
float(poisson.cdf(3, 2))

# Qual a probabilidade de ocorrerem 3 ou menos acidentes no dia
float(poisson.sf(3, 2))