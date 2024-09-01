import pandas as pd
df = pd.DataFrame( {'id' : ['A','A','A','A','A','A','B','B','B','B','B'], 
                    'type' : [1,1,1,1,2,2,1,1,1,2,2], 
                    'book' : ['Math','Math','English','Physics','Math','English','Physics','English','Physics','English','English']})

print("Original DataFrame:")
print(df)
new_df = df[['id', 'type', 'book']].drop_duplicates()\
                         .groupby(['id','type'])['book']\
                         .apply(list)\
                         .reset_index()

new_df['book'] = new_df.apply(lambda x: (','.join([str(s) for s in x['book']])), axis = 1)
print("\nList all unique values in a group:")
print(new_df)
