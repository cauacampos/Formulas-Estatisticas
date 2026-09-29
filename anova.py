import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

# Carregando os dados
tabela = pd.read_csv("anova.csv", sep=";")
tabela.head()

# Boxplot agrupado por remédio
tabela.boxplot(by="Remedio", grid=False)

#Criação de modelo para regressão linear e execução
modelo1 = ols("Horas ~ Remedio", data=tabela).fit()
resultados1 = sm.stats.anova_lm(modelo1)
# p-value = PR(>F)
resultados1

modelo2 = ols("Horas ~ Remedio * Sexo", data=tabela).fit()
resultados2 = sm.stats.anova_lm(modelo2)
# p-value = PR(>F)
resultados2

# Se houver diferença o teste de tukey é válido
mc = MultiComparison(tabela["Horas"], tabela["Remedio"])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)
# resultado_teste.plot_simultaneous()
