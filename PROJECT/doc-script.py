import pyodbc

server = '192.168.0.20'        
database = 'tws'
username = 'Vaish22'
password = 'V@aish22'


conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

try:
    
    conn = pyodbc.connect(conn_str)
    print(" Connected to SQL Server")

    cursor = conn.cursor()

    
    cursor.execute("SELECT TOP 5 * FROM users")

    
    rows = cursor.fetchall()
    print(" First 5 rows in Users table:")
    for row in rows:
        print(row)

except pyodbc.Error as err:
    print(" Database connection or query failed:")
    print(err)

finally:
    if 'conn' in locals():
        conn.close()
        print(" Connection closed")






