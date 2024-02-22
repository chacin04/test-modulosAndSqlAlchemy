from sqlalchemy import create_engine, MetaData, Table
import pprint

pp= pprint.PrettyPrinter(indent=4)
# Conectarse a la base de datos
engine = create_engine('postgresql://postgres:prueba1@localhost:5432/produccion')

# Obtener un objeto MetaData
metadata = MetaData()

# Reflejar las tablas en la base de datos
metadata.reflect(bind=engine)

def nameTables ():
    tablas = metadata.tables.keys()
    for data in tablas:
        print(data)
        data_table = Table(data, metadata, autoload=True, autoload_with=engine)
        pp.pprint(dict(data_table.columns))
        print("")
    else:
        print("*********")
        print(len(tablas))
# Acceder a una tabla específica
mi_tabla = Table('compradores', metadata, autoload=True, autoload_with=engine)

# Realizar una consulta
with engine.connect() as connection:
    resultado = connection.execute(mi_tabla.select())
    
    # Obtener los nombres de las columnas
    column_names = resultado.keys()

    # Obtener los resultados como una lista de diccionarios
    filas_dict = [dict(zip(column_names, fila)) for fila in resultado.fetchall()]

# Imprimir los resultados
# for fila in filas_dict:
#     print(fila)
