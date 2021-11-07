# We want to modify the data in the column 'CANTIDAD' and delete the column 'MATRICULA' in both CSV files
import pandas as pd
url_18 = 'https://raw.githubusercontent.com/AleGL92/PowerBI/master/Entradas_18_19.csv'
d18_19 = pd.read_csv(url_18, encoding = 'latin-1')
print(d18_19.head())

# tiene errores