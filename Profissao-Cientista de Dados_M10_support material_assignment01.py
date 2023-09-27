#!/usr/bin/env python
# coding: utf-8

# # Módulo 10 atividade 1

# Uma instituição financeira quer conhecer melhor o perfil de renda de seus novos clientes para diversos fins, por exemplo, melhor dimensionar o limite de cartões de crédito dos novos clientes, sem necessariamente solicitar olerites ou documentações que impactem na experiência do seu cliente.
# 
# Para isto, conduziu um estudo com alguns clientes, comprovando suas rendas através de olerites e outros documentos, e pretende construir um modelo preditivo para esta renda com base em algumas variáveis que já possui em seu banco de dados.
# 
# As variáveis são intuitivas - note que há uma variável 'index' que é um identificador do cliente e que em geral o ```read_csv``` do pandas coloca também uma variável sequencial.
# 
# Estes dados estão no arquivo ```previsao_de_renda.csv```. Carregue-o em um *dataframe*.
# 
# 1) Avalie a estrutura de correlação das variáveis quantitativas através de um gráfico de "matriz de dispersão" e através da avaliação gráfica da matriz de correlações. Veja se você identifica algum padrão interessante ou que te faça sentido.

# In[4]:


import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('previsao_de_renda.csv')

# Exibir as primeiras linhas do DataFrame para verificar se os dados foram carregados corretamente
print(df.head())


# 2) Avalie um gráfico de dispersão (*scatterplot*) específico para as duas variáveis mais correlacionadas com *renda*.

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('previsao_de_renda.csv')

# Calcular a matriz de correlação
correlation_matrix = data.corr()

# Encontrar as duas variáveis mais correlacionadas com 'renda' (excluindo a própria 'renda')
most_correlated_features = correlation_matrix['renda'].sort_values(ascending=False)[1:3]

# Obter os nomes das duas variáveis mais correlacionadas
variable1, variable2 = most_correlated_features.index

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(data[variable1], data['renda'], alpha=0.5)
plt.title(f'Scatterplot entre {variable1} e Renda')
plt.xlabel(variable1)
plt.ylabel('Renda')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data[variable2], data['renda'], alpha=0.5)
plt.title(f'Scatterplot entre {variable2} e Renda')
plt.xlabel(variable2)
plt.ylabel('Renda')
plt.show()


# 3) Na sua opinião, há outliers na variável renda?

# Sim, no primeiro grafico, parece haver outliers na variável "Renda".
# 
# Os pontos que estão significativamente acima da maioria dos dados, especialmente aqueles perto das marcas de 60.000 e 80.000 no eixo da "Renda", podem ser considerados outliers, pois estão distantes da concentração principal dos pontos. Estes valores muito mais altos de renda, em comparação com a maioria dos dados, são tipicamente considerados outliers em análises visuais.

# No segundo gráfico podemos ver pontos isolados na parte superior, tanto para os indivíduos que não possuem veículo (valores próximos a 0.0 no eixo "posse_de_veiculo") quanto para os que possuem (valores próximos a 1.0). Estes pontos, que representam rendas significativamente mais altas do que a maioria dos dados, podem ser considerados outliers.
# 
# 

# 4) Calcule o logaritmo da variável renda e repita a sequência de análise

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados do arquivo CSV
data = pd.read_csv('previsao_de_renda.csv')

# Calcular o logaritmo natural da variável "renda" e adicionar como uma nova coluna
data['log_renda'] = np.log(data['renda'])

# Calcular a matriz de correlação com a variável "log_renda" incluída
correlation_matrix = data.corr()

# Encontrar as duas variáveis mais correlacionadas com "log_renda" (excluindo a própria "log_renda")
most_correlated_features = correlation_matrix['log_renda'].sort_values(ascending=False)[1:3]

# Obter os nomes das duas variáveis mais correlacionadas
variable1, variable2 = most_correlated_features.index

# Criar o gráfico de dispersão entre "log_renda" e as duas variáveis mais correlacionadas
plt.figure(figsize=(10, 6))
plt.scatter(data[variable1], data['log_renda'], alpha=0.5)
plt.title(f'Scatterplot entre {variable1} e Log da Renda')
plt.xlabel(variable1)
plt.ylabel('Log da Renda')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data[variable2], data['log_renda'], alpha=0.5)
plt.title(f'Scatterplot entre {variable2} e Log da Renda')
plt.xlabel(variable2)
plt.ylabel('Log da Renda')
plt.show()


# 5) A aplicação do LOG você acha que melhorou ou piorou a análise?

# A aplicação do log parece ter melhorado a análise, tornando a distribuição dos dados menos extrema e, possivelmente, tornando mais fácil identificar tendências ou padrões. 
