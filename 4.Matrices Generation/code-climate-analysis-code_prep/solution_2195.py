# import pandas lib as pd
import pandas as pd

# create the data dictionary
data = {'Month' : ['January', 'February', 'March', 'April'],
'Expense': [ 21525220.653, 31125840.875, 23135428.768, 56245263.942]}

# create the dataframe
dataframe = pd.DataFrame(data, columns = ['Month', 'Expense'])

print("Given Dataframe :\n", dataframe)

# round to two decimal places in python pandas
pd.options.display.float_format = '{:.2f}'.format

print('\nResult :\n', dataframe)