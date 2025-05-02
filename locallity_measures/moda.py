import pandas as pd
from scipy.stats import mode
import numpy as np

df = pd.read_csv("../raw/dadosabertos_graduacao_quantitativo-de-alunos.csv", sep=';')
#print(df.head())

nome_curso = df['NomeCurso']

moda, qtd = np.array(mode(nome_curso))

print('A moda eh a cateogira "{}". Qtd de vezes que ocorre: {}'.format(moda[0], qtd))
