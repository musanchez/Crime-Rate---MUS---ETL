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
    
    dim_sql_files = ['DimArea.sql', 'DimDateRptd.sql', 'DimPremis.sql', 'DimStatus.sql', 'DimVictDescent.sql', 'DimVictSex.sql', 'DimWeapon.sql']
    
    origen = 'Crime'
    destino = 'DimensionalCrime'
    
    for sql_file in dim_sql_files:
        
        with open(sql_file, 'r') as file:
            sql_script = file.read()
            
        cursor.execute(f"USE {origen}")
        
        print(f"Ejecutando script '{sql_file}' en la base de datos '{origen}'.")
        cursor.execute(sql_script)
        print(f"Script '{sql_file}' ejecutado correctamente.")
        
        data = cursor.fetchall()
        
        print(f"Cambiando a la base de datos '{destino}' para insertar datos en la tabla.")
        cursor.execute(f"USE {destino}")
        
        table_name = sql_file.split('.')[0]
        print(f"Insertando datos en la tabla '{table_name}'.")
        
        # Verificamos si la tabla tiene una columna identity
        has_identity = table_name in ['DimVictSex', 'DimDateRptd', 'DimVictDescent']
        
        
        if has_identity:
            id = 1
            for row in data:
                row = (id,) + tuple(row)
                print(row)
                insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * (len(row)))})"
                cursor.execute(insert_query, row) 
                print(f"Fila insertada en '{table_name}'")
                id += 1
        else:
            for row in data:
                # Insertamos todos los valores
                insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))})"
                cursor.execute(insert_query, row)
                print(f"Fila insertada en '{table_name}'.")

except Exception as e:
    print(f"Error: {str(e)}")
    
finally:
    cursor.close()
    conn.close()
    print("Conexión cerrada.")
