import pandas as pd

# ruta_local = 'E:\ALEJANDRO\DATA_SCIENCE\POWER_BI\POWER_BI_NACHO\PANEL_PRACTICA\PRUEBAS_GIT\pruebi_exel.csv'
ruta_git = 'https://raw.githubusercontent.com/AleGL92/PowerBI/master/pruebi_exel.csv'
pruebi = pd.read_csv(ruta_git)
pruebi.head()