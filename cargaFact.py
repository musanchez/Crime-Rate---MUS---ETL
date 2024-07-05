import pyodbc
import logging

# Configuración de conexión
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'localhost'
DATABASE_NAME = 'master'

connection_string = f"DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trust_Connection=yes;"

# Configuración de logging
logging.basicConfig(filename='ETLCrime.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Intentar establecer la conexión
    logging.info("Intentando conectar a la base de datos...")
    conn = pyodbc.connect(connection_string, autocommit=True)
    cursor = conn.cursor()

    destino = 'DimensionalCrime'
    sql_file = 'FactCrime.sql'

    # Ejecutar el script SQL para obtener datos
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    
    logging.info(f'Ejecutando script SQL: {sql_file}')
    cursor.execute(sql_script)
    data = cursor.fetchall()

    # Cambiar al contexto de la base de datos destino para inserción
    logging.info(f'Cambiando a la base de datos destino: {destino}')
    cursor.execute(f"USE {destino}")
    
    # Insertar datos en la tabla FactCrime
    for row in data:
        insert_query = f"INSERT INTO FactCrime VALUES ({', '.join(['?'] * len(row))})"
        cursor.execute(insert_query, row)
    
    logging.info(f"Insertados registros en FactCrime")

except Exception as e:
    logging.error(f"Error: {str(e)}")
    print(f"Error: {str(e)}")

finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
        logging.info("Conexión cerrada.")
    else:
        logging.warning("No se pudo establecer la conexión.")

print("Proceso completado.")
