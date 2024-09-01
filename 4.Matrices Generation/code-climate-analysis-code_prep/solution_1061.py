import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('E:\coalpublic2013.xlsx')
df.head(10).plot(kind='bar', figsize=(20,8))
plt.show()
