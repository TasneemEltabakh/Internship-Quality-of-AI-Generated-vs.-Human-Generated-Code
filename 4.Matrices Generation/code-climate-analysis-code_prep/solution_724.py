import pandas as pd
df = pd.DataFrame({
    'name_code': ['Company','Company a001','Company 123', '1234', 'Company 12'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
print("\nWhether all characters in the string are alphanumeric?")
df['name_code_is_alphanumeric'] = list(map(lambda x: x.isalnum(), df['name_code']))
print(df)
