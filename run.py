import pandas as pd
import numpy as np


# Read the CSV file
df = pd.read_csv('data.csv', encoding='utf-8')

# Replace NaN with None
df.replace({np.nan: None}, inplace=True)

# Create INSERT statement
columns = ','.join(df.columns)
sql_statement = f'INSERT INTO table_name ({columns}) VALUES '
for row in df.itertuples(index=False, name=None):
    values = ','.join(f'"{v}"' if v else 'NULL' for v in row)
    query = f'({values}),\n'
    sql_statement += query

# Write SQL statement to file
with open('script.sql', 'w', newline='', encoding='utf-8') as file:
    file.write(sql_statement[:-2])
    file.write(';')
