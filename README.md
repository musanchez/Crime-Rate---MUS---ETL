# Proyecto ETL Crime Data

## Descripción

Este proyecto tiene como objetivo extraer, transformar y cargar datos de crímenes en un modelo dimensional para análisis posterior. El proyecto está compuesto por varios scripts que se ejecutan de manera secuencial para lograr este objetivo.

## Estructura del Proyecto

- **ETLCrime.py**: Script principal que orquesta la ejecución de los demás scripts.
- **CrimeData.py**: En este script se crean las tablas del modelo dimensional y la segunda tabla donde caerán los datos limpios y transformados en otra base de datos. El script puede ejecutarse múltiples veces, cada vez que el programa se ejecuta las tablas dropean y crean nuevamente, además de no existir la segunda base de datos donde se encuentra nuestro modelo dimensional será creada.
- **extraccion.py**: Este script se encarga de la limpieza y transformación de datos.
- **cardaDim.py**: Script que carga los datos transformados en las tablas dimensionales.
- **cargaFact.py**: Script que carga los datos en la tabla de hechos.
- **extras**: Carpeta que contiene el diagrama del modelo dimensional y el enlace donde puede descargar el archivo .bak de la base de datos con CSV importado.

## Ejecución del Proyecto

Para ejecutar el proyecto, simplemente ejecuta el script principal:
```bash
python ETLCrime.py
```

## Configuración de la Cadena de Conexión

He utilizado `localhost` en mi cadena de conexión para el nombre del servidor, pero ten en cuenta que el `DRIVER_NAME` varía en dependencia del equipo en el que se ejecute el programa.

### Configuración en Mi Equipo

Para usar SQLAlchemy, el `DRIVER_NAME` es `ODBC Driver 17 for SQL Server`.  
Para usar `pyodbc`, el `DRIVER_NAME` es `SQL SERVER`.
