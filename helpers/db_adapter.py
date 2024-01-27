import pyodbc

class DbAdapter:

    @classmethod
    def get_all(cls):
        server = 'aurorasqlserverdev.database.windows.net'
        database = 'lbrdev'
        username = 'aurorasqladmin'
        password = 'password'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database}')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * from dbo.Books")
        row = cursor.fetchone()
        while row:
            print(str(row[0] + " " + str(row[1])))
            row = cursor.fetchone()
        return row

    @classmethod
    def get_by_id(cls,id):
        server = 'aurorasqlserverdev.database.windows.net'
        database = 'lbrdev'
        username = 'aurorasqladmin'
        password = 'password'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database}')
        cursor = cnxn.cursor()
        cursor.execute(f'SELECT * from dbo.Books where id={id}')
        row = cursor.fetchone()
        while row:
            print(str(row[0] + " " + str(row[1])))
            row = cursor.fetchone()
        return row

    @classmethod
    def delete_by_id(cls,id):
        server = 'aurorasqlserverdev.database.windows.net'
        database = 'lbrdev'
        username = 'aurorasqladmin'
        password = 'password'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database}')
        cursor = cnxn.cursor()
        cursor.execute(f'delete from dbo.Books where id={id}')
        row = cursor.fetchone()
        while row:
            print(str(row[0] + " " + str(row[1])))
            row = cursor.fetchone()

