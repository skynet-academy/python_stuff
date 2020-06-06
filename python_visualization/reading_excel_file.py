import xlrd 
from pprint import pprint
file = 'Canada.xlsx'

wb = xlrd.open_workbook(filename=file)
ws = wb.sheet_by_name('Canada by Citizenship')

dataset = []

for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r,c).value)
    dataset.append(col)

pprint(dataset)

