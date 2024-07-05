import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'localhost'
DATABASE_NAME = 'master'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
try:
    conn = pyodbc.connect(connection_string, autocommit=True)
    cursor = conn.cursor()
    destino = 'DimensionalCrime'
    sql_file = 'FactCrime.sql'

    with open(sql_file, 'r') as file:
        sql_script = file.read()
        cursor.execute(sql_script)
        data = cursor.fetchall()
    
    cursor.execute(f"USE {destino}")
    
    for row in data:
        insert_query = f"INSERT INTO FactCrime VALUES ({', '.join(['?'] * len(row))})"
        cursor.execute(insert_query, row)
    
    
    
except Exception as e:
    print(f"Error: {str(e)}")
    
finally:
    cursor.close()
    conn.close()
    print("Conexion cerrada.")