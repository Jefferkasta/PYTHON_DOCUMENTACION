#Funcion
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ['Jeffer',"Karla",'Petro','Ximena']
desplegarNombres(nombres)
desplegarNombres('Jeffer')
#un solo numero lo reconoce como INT y no es un valor iterable, si le ponemos doble parentecis (()) la funcion lo toma como una tupla
#aca lo reconoce como una tupla con ()
desplegarNombres((10,25))
#aca lo reconoce como una lista con [] 
desplegarNombres([10,25])

##VIDEO 82 UDEMY##