import sys
import pandas as pd
import psycopg2

class Converter:
    """
    This class converts the excel file into sql language
    """
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
        
    def excel_to_csv(self):
        self.df = pd.read_excel(self.file_name, sheet_name=self.sheet_name)
        self.df.to_csv(self.file_name + '.csv', index=False)

    def csv_to_sql(self):
        try:
            conn = psycopg2.connect(host='localhost', 
                    port='5432', 
                    dbname='testdb',
                    user='postgres',
                    password='123456'
                    )
            cur = conn.cursor()
            #cur.execute(''' CREATE TABLE {} ''')
            csv_file = open(r'/home/nico/projects/python_stuff/test1.xlsx.csv', 'r')
            table_name = 'my_table'
            cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), csv_file)
            cur.execute("commit;")
            print("the data was loaded into {}!".format(table_name))
            cur.execute("COPY (SELECT * FROM {}) TO '/tmp/result_sql.xlsx' WITH CSV HEADER;".format(table_name))
            print("the query was translated into a excel file")
            conn.close()
            print("DataBase connection is closed.")

        except Exception as e:
            print("Error: {}".format(str(e)))
            sys.exit(1)






