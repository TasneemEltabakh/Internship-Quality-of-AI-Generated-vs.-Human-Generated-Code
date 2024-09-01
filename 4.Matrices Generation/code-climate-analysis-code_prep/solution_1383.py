import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('E:\coalpublic2013.xlsx')
sorted_by_production = df.sort_values(['Production'], ascending=False).head(10)
sorted_by_production['Production'].head(10).plot(kind="barh")
plt.show()
