import numpy as np
from scipy.stats import chi2_contingency

# Criação de matriz com dados para teste
novela = np.array([[19, 6], [43, 32]])
novela

# Segundo valor é p-value
# Se p-value > 0.05 então não temos evidências para recusar a hipótese nula (h0)
chi2_contingency(novela)

novela2 = np.array([[22, 3], [43, 32]])
novela2

# Se p-value < 0.05 então temos evidências para recusar a hipótese nula (h0)
chi2_contingency(novela2)
