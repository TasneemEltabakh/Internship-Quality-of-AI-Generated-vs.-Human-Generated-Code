import pandas as pd
from datetime import datetime
import numpy as np


range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
freq ='Min')
print(range_date)