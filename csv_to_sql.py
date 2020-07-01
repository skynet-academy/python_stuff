import psycopg2

conn = psycopg2.connect("host='localhost' port='5432' dbname='testdb' user='postgres' password='my password' ")
cur = conn.cursor()
f = open(r'/home/nico/projects/python_stuff/fileName.csv', 'r')
cur.copy_from(f, my_new_table, sep=',')
f.close()



