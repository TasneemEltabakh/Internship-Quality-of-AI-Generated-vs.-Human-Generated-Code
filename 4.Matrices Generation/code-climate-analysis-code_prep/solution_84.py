import pandas as pd
df = pd.DataFrame({
    'company_code': ['Company','Company a001', '2055', 'abcd', '123345'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
	
print("Original DataFrame:")
print(df)
print("\nNumeric values present in company_code column:")
df['company_code_is_digit'] = list(map(lambda x: x.isdigit(), df['company_code']))
print(df)

