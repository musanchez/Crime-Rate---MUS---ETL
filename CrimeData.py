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
    database = 'DimensionalCrime'
        
    sql_files = ['CrimeData.sql', 'DimensionalCrime.sql', 'DropStatementsDimCrime.sql', 'DimensionalCrimeTables.sql']

    for file_name in sql_files:
        with open(file_name, 'r') as file:
            sql_script = file.read()
        cursor.execute(sql_script)
    
   
except Exception as e:
    print(f"Error: {str(e)}")


finally:
    cursor.close()
    conn.close()
    print("Conexion cerrada.")