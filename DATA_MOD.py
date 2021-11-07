# We want to modify the data in the column 'CANTIDAD' and delete the column 'MATRICULA' in both CSV files
import pandas as pd

url_18_19 = 'E:\ALEJANDRO\DATA_SCIENCE\POWER_BI\POWER_BI_NACHO\PANEL_PRACTICA\PRUEBAS_GIT\Entradas_18_19.csv'
url_20 = 'E:\ALEJANDRO\DATA_SCIENCE\POWER_BI\POWER_BI_NACHO\PANEL_PRACTICA\PRUEBAS_GIT\Entradas_20.csv'
d18_19 = pd.read_csv(url_18_19, header = 0, sep = ';')
d20 = pd.read_csv(url_20, header = 0, sep = ';')

# print(d18_19.head(5))
# print(d20.head(5))

url_18_19['cantidad'] = url_18_19['cantidad']*1000
url_20['cantidad'] = url_20['cantidad']*1000

url_18_19 =  url_18_19.drop('matricula', 1)
url_20 = url_20.drop('matricula', 1)
