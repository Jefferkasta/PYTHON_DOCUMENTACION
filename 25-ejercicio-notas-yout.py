'''Realizar un programa que conste de una clase llamada alumno que tenga como atributos el nombre y la nota del alumno.
Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''
class Alumno:
    #inicializamos los atributos
    def __init__(self):
        self.nombre = input('Nombre Alumno:')
        self.nota = input('Ingrese la nota: ')
        
    def imprimir(self):
        print("Alumno: ", self.nombre)
        print("Nota:", self.nota)
        print("")
        
    def resultado(self):
        if float(self.nota < 5):
            print("El estudiante reprobo")
        else:
            print("El estudiante aprobo con: ",{self.nota})
            
objetoAlumno = Alumno()
objetoAlumno.imprimir()
objetoAlumno.resultado()