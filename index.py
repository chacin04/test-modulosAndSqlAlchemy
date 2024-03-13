from sqlalchemy import create_engine, MetaData, Table
import pprint

pp= pprint.PrettyPrinter(indent=4)
# Conectarse a la base de datos
engine = create_engine('postgresql://postgres:clavechula123@10.1.30.159:5432/produccion')

# Obtener un objeto MetaData
metadata = MetaData()

# Reflejar las tablas en la base de datos
metadata.reflect(bind=engine)

# Acceder a una tabla específica
mi_tabla = Table('order_sales_2', metadata, autoload=True, autoload_with=engine)

# Realizar una consulta
with engine.connect() as connection:
    resultado = connection.execute(mi_tabla.select().limit(25000))
    
    # Obtener los nombres de las columnas
    column_names = resultado.keys()

    # Obtener los resultados como una lista de diccionarios
    filas_dict = [dict(zip(column_names, fila)) for fila in resultado.fetchall()]

# Imprimir los resultados
for fila in filas_dict:
    pp.pprint(fila)
