from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de cair cara 3 vezes?
# eventos esperados, experimentos, probabilidade
prob = binom.pmf(3, 5, 0.5)
prob

# Passar por 4 sinais com 4 tempos, qual a probabilidade de pegar sinal verde em nenhum, 1, 2, 3 ou 4 vezes seguidas?
binom.pmf(0, 4, 0.25) + binom.pmf(1, 4, 0.25) + binom.pmf(2, 4, 0.25) + binom.pmf(3, 4, 0.25) + binom.pmf(4, 4, 0.2)

# E se forem 4 sinais de 2 tempos?
binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
binom.cdf(4, 4, 0.25)

# Na prova de 12 questões, qual a probabilidade de acertar 7 questões sendo que cada uma tem 4 alternativas?
binom.pmf(7, 12, 0.25)

# Prob de acertar as 12
binom.pmf(12, 12, 0.25)
