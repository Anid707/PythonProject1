import pyodbc

server = 'aurorasqlserverdev.database.windows.net'
database = 'lbrdev'
username = 'aurorasqladmin'
password = 'password'
driver = '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database}')
cursor = cnxn.cursor()
cursor.execute("SELECT * from dbo.Books where id=697")
row = cursor.fetchone()
while row:
    print(str(row[0] + " " + str(row[1])))
    row = cursor.fetchone()
    