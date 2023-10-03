#definir una clase
class persona:
    #para agregar caracteristicas o metodos a la clase se necesita llamar una funcion llamada __init__
    #__init__ es un metodo inicializador, es un metodo especial llamada "donder"
    #esta funcion init tiene como default el parametro self, es referencia al objeto que se crea
    
    def __init__(self):
        #se crea atributo de instancia
        self.nombre = "Jefferson"
        self.apellido = "Vega Castañeda"
        self.edad = 27
#creamos primer objeto, creando una variable para asignar el objeto
persona1 = persona()
#llamamos los atributos con el objeto
print(persona1.nombre) 
print(persona1.apellido)
print(persona1.edad)

    