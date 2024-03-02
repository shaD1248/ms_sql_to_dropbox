import pyodbc

# SQL Server connection details
sql_server = 'SABA\\TNC'
database = 'dbo'
username = 'SABA\\hp'
password = ''
driver= '{ODBC Driver 17 for SQL Server}'  # Example driver, adjust based on your server

# SQL query
sql_query = 'SELECT [A_Code], [A_Name], [Exist] FROM [Holoo1].[dbo].[ARTICLE]'  # Adjust this to your query

def fetch_data_from_sql():
    conn_string = f'DRIVER={driver};SERVER={sql_server};DATABASE={database};UID={username};PWD={password}'
    with pyodbc.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall(), [column[0] for column in cursor.description]