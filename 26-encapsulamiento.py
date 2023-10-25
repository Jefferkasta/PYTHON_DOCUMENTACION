#encapsulamos datos con el metodo GET y el decorador property para que solo podamos recuperar el atributo con la funcion GET

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    #creacion del metodo GET con el decorador property
    @property
    def nombre(self):
        return self._nombre
    #creacion del metodo SET con el decorador
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
      
    def mostrar_detalle(self):
        print(f'persona: {self._nombre} {self.apellido} {self.edad}')
        
persona1 = Persona('Juan', 'Ramirez', 26)
print(persona1.nombre)      #Traemos el dato con el metodo GET
persona1.nombre = 'Carlos'  #Aca con modificado con el metodo SET
print(persona1.nombre)
