import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook


arquivo = 'divVoVera.xlsx'

tabela = pd.read_excel(arquivo)

motivoDivida = tabela['Motivo Divida'] [17]

print(tabela)