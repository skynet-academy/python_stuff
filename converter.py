import pandas as pd


def excel_to_csv(fileName, sheet_name):
    df = pd.read_excel(fileName, sheet_name= sheet_name)
    df.to_csv( fileName + '.csv', index=False)
    print("the file {} was converted successfully to CSV".format(fileName) )


def csv_to_sql():
    pass




