import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging
import re

# Configuración de la conexión
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'localhost'
DATABASE_NAME = 'Crime'
connection_string = f'mssql+pyodbc://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}&trusted_connection=yes'

# Configuración del registro de logs
logging.basicConfig(filename='extraccion.log', level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    # Intentando conectar a la base de datos
    logging.info("Intentando conectar a la base de datos...")
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Leer y ejecutar el archivo SQL
    with open('extract.sql', 'r') as file:
        sql = file.read()

    logging.info(f'Ejecutando SQL: {sql}')
    data = pd.read_sql(sql, engine)
    logging.info('Extracción exitosa')
    print('Extracción exitosa')

    # Limpieza y transformación de datos
    data['Date_Rptd'] = pd.to_datetime(data['Date_Rptd']).dt.date
    data['DATE_OCC'] = pd.to_datetime(data['DATE_OCC']).dt.date
    data['TIME_OCC'] = data['TIME_OCC'].astype(int)
    data['Weapon_Used_Cd'] = data['Weapon_Used_Cd'].fillna(0).astype(int)
    data['Weapon_Desc'] = data['Weapon_Desc'].fillna('No aplica')
    data['Vict_Sex'] = data['Vict_Sex'].fillna('No aplica')
    data['Vict_Descent'] = data['Vict_Descent'].fillna('No aplica')
    data['Mocodes'] = data['Mocodes'].fillna('No aplica')
    data['Vict_Age'] = data['Vict_Age'].fillna(0).astype(int)
    data.loc[(data['Vict_Age'] < 0) | (data['Vict_Age'] > 99), 'Vict_Age'] = 0
    data['Vict_Sex'] = data['Vict_Sex'].fillna('No aplica').str.upper()
    data['Vict_Descent'] = data['Vict_Descent'].fillna('No aplica').str.upper()
    data['LOCATION'] = data['LOCATION'].apply(lambda x: re.sub(r'\s+', ' ', str(x).strip()))
    data['Cross_Street'] = data['Cross_Street'].apply(lambda x: re.sub(r'\s+', ' ', str(x).strip()))
    data['LAT'] = pd.to_numeric(data['LAT'], errors='coerce').fillna(0).astype(float)
    data['LON'] = pd.to_numeric(data['LON'], errors='coerce').fillna(0).astype(float)
    data.drop(columns=['Crm_Cd_1', 'Crm_Cd_2', 'Crm_Cd_3', 'Crm_Cd_4'], inplace=True)
    logging.info('Datos limpios y transformados')

    # Carga de datos a la base de datos final en fragmentos
    logging.info('Iniciando carga de datos...')
    chunksize = 10000  # Número de filas por fragmento
    for i in range(0, len(data), chunksize):
        chunk = data.iloc[i:i + chunksize]
        chunk.to_sql('CrimeData', engine, if_exists='append', index=False)
        logging.info(f'Fragmento {i//chunksize + 1} de {len(data)//chunksize + 1} cargado')

    logging.info('Datos cargados a la base de datos final de SQL Server')
    print('Datos cargados exitosamente')

except SQLAlchemyError as e:
    logging.error(f"Error: {e}")
    print(f"Error: {e}")

finally:
    try:
        session.close()
        logging.info('Conexión cerrada')
    except SQLAlchemyError as e:
        logging.error(f"Error al cerrar la conexión: {e}")
    print("Conexión cerrada")
