import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

m = np.array([[0.9, 0.53, 1.00, 0.32], 
              [-0.2, 1., -0.458, 0.49],
              [0.1, 0.004, 1.5, 0.195]])

df = pd.DataFrame(m)

print(df)

sns.heatmap(df, annot=True, cmap='viridis')

plt.title('Heatmap test')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('heatmap_example1.png')