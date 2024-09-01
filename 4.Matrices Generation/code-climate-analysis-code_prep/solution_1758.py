# import required libraries
import pandas as pd
import re

# creating Dataframe with
# name and their comments
df = pd.DataFrame({
'Name' : ['Akash', 'Ashish', 'Ayush',
'Diksha' , 'Radhika'],

'Comments': ['Hey! Akash how r u' ,
'Why are you asking this to me?' ,
'Today, what we are going to do.' ,
'No plans for today why?' ,
'Wedding plans, what are you saying?']},

columns = ['Name', 'Comments']
)

# show the Dataframe
df