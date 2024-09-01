import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
df[df['hire_date'] >='20070101']
