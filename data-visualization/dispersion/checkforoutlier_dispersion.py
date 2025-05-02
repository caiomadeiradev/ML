import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../raw/dadosabertos_graduacao_quantitativo-de-alunos.csv", sep=';')
# print(df.head())

cc_df = df[df['NomeCurso'] == "CIÊNCIA DA COMPUTAÇÃO"]
# print(cc_df.head())
print("size:", cc_df.size)
# print(cc_df.tail())

"""
O ano eh repetido pois representa dois semestres. 
Vamos junta-los.
"""
evadidos = pd.concat([cc_df["Ano"], cc_df["Evadidos"]], axis=1)
# print(evadidos.head())
evadidos_agrupados = evadidos.groupby("Ano").sum().reset_index()
print(evadidos_agrupados)

sns.scatterplot(x="Evadidos", y="Ano", data=evadidos, hue="Evadidos")

plt.title("Grafico de Dispersao - Evadidos por ano em Ciência da Computação na UFRGS")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
plt.savefig("dispersion_graph_ufrgs_cc_hue=evadidos.png")
