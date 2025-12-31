import pandas as pd
data_string = """ID,Gender,Salary,Country,Company
1,Male,15000,India,Google
2,Female,45000,China,NaN
3,Female,25000,India,Google
4,NaN,NaN,Australia,Google
5,Male,NaN,India,Google
6,Male,54000,NaN,Alibaba
7,NaN,74000,China,NaN
8,Male,14000,Australia,NaN
9,Female,15000,NaN,NaN
10,Male,33000,Australia,NaN"""

with open('salary.csv', 'w') as out:
    out.write(data_string)

df = pd.read_csv('salary.csv')

print('Salary Dataset:\n', df)

print('Missing Data\n', df.isna())

print('Missing Data\n', df.isnull())

print('Filter based on columns: \n', df[df.isnull().any(axis=1)])

print('Sum up the missing values: \n', df.isnull().sum())
