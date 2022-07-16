import pyodbc
import pandas as pd
print(pyodbc.drivers())
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


DRIVER_NAME = 'ODBC Driver 18 for SQL Server'
SERVER_NAME = '172.17.0.2'
DATABASE_NAME = 'Person'
username = 'sa'
password = 'password'

"""
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};" + "SERVER=127.0.0.1,1433;"
                                                "DATABASE=AdventureWorksDW2019;"
                                                "UID=hanrui;"
                                                "PWD=password;")

print("=======Connected======")
cur = conn.cursor()
query = "select  t.name as table_name from sys.tables t where t.name in ('Product','ProductSubcategory','ProductSubcategory','ProductCategory','SalesTerritory','FactInternetSales')"
cur.execute(query)
src_tables = cur.fetchall()
print(conn)
print(src_tables[:2])

for tbl in src_tables:
    # query and load save data into dataframe
    # df =pd.read_sql_query(f'select * from {tbl[0]}', conn)

    print(tbl)

src_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER=127.0.0.1,1433;'
                                  'DATABASE=AdventureWorks2019;'
                                  'UID=etl;'
                                  'PWD=password;')
        src_cur = src_conn.cursor()
        # execute query
        query = "select  t.name as table_name from sys.tables t where t.name in ('Product','ProductSubcategory','ProductSubcategory','ProductCategory','SalesTerritory','FactInternetSales')"
        src_cur.execute(query)
        src_tables = src_cur.fetchall()
        #print(src_tables)
        for tbl in src_tables:
            print(tbl[0])
            #df = pd.read_sql_query(f"select * from {tbl[0]}", src_conn)
            #print(df.head())
"""
engine = create_engine(f'postgresql://postgres:password@127.0.0.1:5432/postgres')
connection = engine.connect()
print(connection)
query = "select * from postgres.public.student"
result = engine.execute(query)
for i in result:
    print(i)



