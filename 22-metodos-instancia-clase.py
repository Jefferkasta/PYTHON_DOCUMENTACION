class Class_persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad 


    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona2 = Class_persona('Jefferson','Vega Castañeda', 28)
persona2.mostrar_detalle()