from sklearn.datasets import load_wine
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
"""
load_wine(): faz parte da sklearn.datasets e serve
pra carregar um DATASET REAK usando em tarefas de 
MACHINE LEARNING supervisionado.
"""

wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target

# exploring dataset
print(df.head()) 
print("-----------------"*10)
# print(df.describe())
# print("-----------------"*10)
# print(df.info())

# normalization and padronization
"""
Normalization


Normalizacao (ou feature scaling) eh uma tenica pra colocar
os dados num intervalo comum, geralmente entre (0 e 1).

Ex.:
    Imagine que temos dois atributos numericos?
        idade: varia entre 18 a 60
        salario: varia entre 1000 e 10000

Se um algoritimo calcular a distancia entre pontos (como KNN, SVM, redes neurais...),
o salario tera muito mais PESO, porque seus valores sao maiores.

    PS: Quando dizemos que uma variavel tem mais peso, matematicamente estamos dizendo que ela INFLUENCIA
    MAIS O CALCULO, especialmente em metricas de distancia ou em combinacoes lineares.

    PS: A distancia entre dois pontos aqui eh a Distancia Euclidiana (usada por KNN, K-Means, etc)

E porque calculamos a distancia? O que o valor da distancia representa?
    A distancia ente dois vetores x e y representa o quao diferentes eles sao no espaco das variaveis.

Isso eh um problema pois a diferenca da escal desbalanceia o aprendizado do modelo.


"""
normalizer = MinMaxScaler()
df_norm = pd.DataFrame(normalizer.fit_transform(df.iloc[:, :-1]), columns=wine.feature_names)
print(df_norm.head())