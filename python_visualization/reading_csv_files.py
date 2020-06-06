import csv

filename = 'AllBirdsv4.csv'

data = []

try: 
    with open(filename) as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        header = reader.__next__()
        data = [row for row in reader]
except csv.Error as e:
    print("Error reading CSV file at line %s: %s"%(reader.line_num, e))
    sys.exit(-1)
if header:
    print(header)
    print('--*--'*10)
for datarow in data:
    print(datarow)

