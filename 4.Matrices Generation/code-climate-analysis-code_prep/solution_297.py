import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in @Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
    })
print("Original DataFrame:")
print(df)
def find_at_word(text):
    word=re.findall(r'(?<[emailprotected])\w+',text)
    return " ".join(word)

df['at_word']=df['tweets'].apply(lambda x: find_at_word(x))
print("\Extracting @word from dataframe columns:")
print(df)
