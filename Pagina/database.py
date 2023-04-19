from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mercadopago import *
import logging
logging.getLogger('sqlalchemy').setLevel(logging.WARNING)

Base = declarative_base()

class Ingredientes(Base):
    __tablename__="costos"
    # Define las columnas de la tabla con su nombre y tipo de dato
    nombre = Column("nombre", String, primary_key=True)
    precio = Column("precio", Integer)
    link = Column("link", String, default = '')
    
    #Constructor de clases
    def __init__(self, nombre,precio, link):
        self.nombre = nombre
        self.precio = precio
        self.link = link
    
    #Define como se printea
    def __repr__(self):
        return f"{self.nombre} {self.precio} {self.link} \n"
#Crea la base en sqlite
engine = create_engine("sqlite:///mydb.db", echo=True)

# Crea la tabla en la base de datos
Base.metadata.create_all(bind=engine)

# Crea una clase de sesión que se utiliza para interactuar con la base de datos
Session = sessionmaker(bind=engine)

# Crea una instancia de la sesión para comenzar a interactuar con la base de datos
session = Session()


def agregar_ingrediente(nombre, precio, url):
    """
    Agrega un nuevo ingrediente a la tabla
    """
# Busca un registro con el mismo nombre en la tabla Ingredientes
    ingrediente_existente = session.query(Ingredientes).filter(Ingredientes.nombre == nombre).first()

    if ingrediente_existente:
        # Si ya existe un registro con ese nombre, actualiza su precio
        ingrediente_existente.precio = precio
        ingrediente_existente.link = url
    else:
        # Si no existe, crea un nuevo objeto Ingredientes con los valores recibidos como argumentos
        nuevo_ingrediente = Ingredientes(nombre=nombre, precio=precio, link=url)
        # Agrega el objeto a la sesión
        session.add(nuevo_ingrediente)

    # Guarda los cambios en la base de datos
    session.commit()


def updatear_precios():
    """
    Usando el diccionario "nuevo", refresca los precios
    Si hay un link caido te tira este error: AttributeError: type object 'Ingredientes' has no attribute 'medida'
    """
#NUEVO es el dict con PRODUCTO Y LINK
    for producto, url in nuevo.items():
        #La formula producto_precio returnea el producto con el precio en kg
        for producto, precio in producto_precio(producto, url).items():
            #Agrega a la tabla los productos con su precio
            agregar_ingrediente(producto, precio, url)


def buscar_ingrediente(nombres):
    """
    Devuelve el  precio por gramo/unidad del ingrediente
    """
    #Query(Ingredientes) para eleigr la tabla y columnas, dps la propiedad es lo que le quieras hacer:
    #.Filer--> Filtro
    #.All todo
    #Lo va a queryear como vos lo inicializaste en __repr__
    result = session.query(Ingredientes.precio).filter(Ingredientes.nombre==nombres).all()
    #Primero loopeas por el primer resultado y dps el index 0 del primer resultado, si no te da error xq etas trabajando con otro tipo de dato 
    for r in result:
        precio_kg = int(r[0]) #PRECIO
        return precio_kg


def mostrar_tabla():
    """
    Muestra TODOS los ingredientes ocn su nombre, precio y publicacion
    """
    result = session.query(Ingredientes).order_by(Ingredientes.nombre).all()
    return result

