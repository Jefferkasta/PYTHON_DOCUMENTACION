class Class_persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad 
persona2 = Class_persona("Jeffer","Castañeda",28)
print(f"persona 1: {persona2.nombre} {persona2.apellido} {persona2.edad}")

#modificamos valores directamente
persona2.nombre = 'JEFFERSON'
persona2.apellido = 'VEGA CASTAÑEDA'
persona2.edad = 29
print(f"persona 1: {persona2.nombre} {persona2.apellido} {persona2.edad}")
#modificando sus atributos por medio de la variable