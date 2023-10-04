#calculadora de impuesto//
#Crea una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
#formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

#proporcione el pago sin impuesto: 1000
#proporcione el monto del impuesto: 16
#Pago con impuesto: 1160.0

#defino la funcion
def calculadora(pago_sin_impuesto, impuesto):
    #esta es la formula proporcionado por el creador del curso
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    #creo el print que dara el resultado pedido
    return pago_total
    #esta sera la funcion con el codigo correspondiente

#fuera de la funcion invoco a las variables que estan pedidas en la funcion, y les inserto un "input"  para pedir los datos al usuario   
pago_sin_impuesto = float(input("Ingrese el pago con impuesto:"))
impuesto = float(input("Ingrese el impuesto:"))
#al ya tener los datos ingresados por el usuario invoco la funcion con la variable pago_sin_impuesto
pago_con_impuesto = calculadora(pago_sin_impuesto,impuesto)
print("pago con impuesto: ",pago_con_impuesto)
    