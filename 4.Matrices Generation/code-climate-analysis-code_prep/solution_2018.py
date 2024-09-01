# importing required libraries
import pandas as pd
import re


# creating Dataframe with column
# as name and common_comments
df = pd.DataFrame(
{
'name' : ['Akash', 'Ayush', 'Diksha',
'Priyanka', 'Radhika'],

'common_comments' : ['hey buddy meet me today ',
'sorry bro i cant meet',
'hey akash i love geeksforgeeks',
'twiiter is the best way to comment',
'geeksforgeeks is good for learners']
},

columns = ['name', 'common_comments']
)
# printing Dataframe
df