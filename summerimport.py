import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='root', password='Maximu$pyris', host='localhost', database='terrordb')
cursor = cnx.cursor()
csv_data = pd.read_csv('Users/briansui/Downloads/terror_org_names.csv') 

for row in csv_data.iterrows():
    list = row[1].values
    cursor.execute("INSERT INTO groups(org) VALUES('%s')" % tuple(list))

cursor.close() 
cnx.close() 