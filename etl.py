import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


print(pyodbc.drivers())

DRIVER = 'ODBC Driver 18 for SQL Server'
SERVER = '127.0.0.1,1433'  # localhost
DATABASE = 'AdventureWorks2019'
USERNAME = 'hanrui'
PASSWORD = 'password'
TABLES = ('Department', 'SalesPerson', 'Customer', 'Shift', 'EmailAddress', 'Person')


def extract():
    try:
        # db_connect_url = f"mssql+pyodbc://hanrui:password@127.0.0.1:1433/AdventureWorks2019?driver={DRIVER}"
        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1,1433;DATABASE=AdventureWorks2019;UID=etl;PWD=password;"
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect":connection_string})
        engine = create_engine(connection_url)
        connection = engine.connect()
        query_find_tables = F"select  t.name, t.schema_id as table_name from sys.tables t where t.name in {TABLES}"
        tables = engine.execute(query_find_tables)
        for table in tables:
            print(table)
            table_name = table[0]
            schema_id = table[1]
            schema = ''
            query_find_schema = f"select name from sys.schemas where schema_id = {schema_id}"
            schema_name_result = engine.execute(query_find_schema)
            for schema_name in schema_name_result:
                schema = schema_name['name']
            query_data_from_table = f"select * from {schema}.{table_name}"
            df = pd.read_sql_query(query_data_from_table, engine)
            load(df, table_name)

    except Exception as err:
        print("Data extract error: " + str(err))
    finally:
        connection.close()


def load(df, table):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://postgres:password@127.0.0.1:5432/testdb')
        connection = engine.connect()
        print(f'Importing rows {rows_imported} to {rows_imported + len(df)} ... for table {table}')
        # load df to postgres
        df.to_sql(f'loaded_from_mssql_{table}',engine, if_exists='replace')
        rows_imported += len(df)
        print(f"{table} imported successfully! ")
    except Exception as err:
        print("Data load error: " + str(err))
    finally:
        connection.close()

def main():
    extract()


if __name__ == '__main__':
    main()
