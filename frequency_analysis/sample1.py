"""
Nota: Apenas o exemplo do calculo de frequencia.
Esse nao eh o tipo de caso que usualmente usamos o calculo de frequencia. 
Usa-se mais sobre o meta atributo (atributo alvo).
"""
import numpy as np
import pandas as pd

df = pd.read_csv("../raw/dadosabertos_graduacao_quantitativo-de-alunos.csv", sep=";")

nome_curso = df['NomeCurso']

frequency = (nome_curso == 'ARQUIVOLOGIA').sum() / float(nome_curso.size)

print("Frequência da categoria 'ARQUIVOLOGIA' eh ", frequency * 100, '%')
