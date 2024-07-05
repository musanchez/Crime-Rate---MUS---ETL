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

    database = 'DimensionalCrime'
    sql_files = ['CrimeData.sql', 'DimensionalCrime.sql', 'DropStatementsDimCrime.sql', 'DimensionalCrimeTables.sql']

    for file_name in sql_files:
        with open(file_name, 'r') as file:
            sql_script = file.read()
        
        # Ejecutar el script SQL
        logging.info(f'Ejecutando script: {file_name}')
        cursor.execute(sql_script)
        logging.info(f'Script ejecutado correctamente: {file_name}')

except Exception as e:
    logging.error(f"Error: {str(e)}")

finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
        logging.info("Conexión cerrada.")
    else:
        logging.warning("No se pudo establecer la conexión.")

print("Proceso completado.")
