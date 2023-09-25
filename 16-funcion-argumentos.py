#Funcion que guarda una "tupla" como parametros sin un limite conocido (* porquen o sabemos cuantos vamos a añadir)
def tuplaProductos(*productos):
    for producto in productos:
        print(producto)
tuplaProductos('tomate','cebolla','lechuga')

#Funcion que guarda un parametro "diccionario"

def listaProductos(**productos):
    for nombre, valor in productos.items():
        print(f'{nombre}:{valor}')

listaProductos(Tomate=1300,Cebolla=900)
    