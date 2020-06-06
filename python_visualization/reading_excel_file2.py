from datetime import datetime
from xlrd import open_workbook, xldate_as_tuple

cell = sheet.cell(1,0)
print(cell)
print(cell.value)
print(cell.ctype)
if cell.ctype == xlrd.XL_CELL_DATE:
    date_value = xldate_as_tuple(cell.value, book.datemode)
    print(datetime(*date_value))


