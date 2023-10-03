class class_persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad 
persona2 = class_persona("Jeffer","Castañeda",28)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)